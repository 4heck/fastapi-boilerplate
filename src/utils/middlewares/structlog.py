import time
import uuid

from core import settings
from starlette.middleware.base import BaseHTTPMiddleware

from structlog import get_logger

logger = get_logger(__name__)


def get_request_header(request, header_key, meta_key):
    return request.headers.get(header_key) or request.headers.get(meta_key)


def get_vars(request):
    return {
        "correlation_id": get_request_header(
            request, "x-correlation-id", "HTTP_X_CORRELATION_ID"
        ),
        "request_id": get_request_header(
            request, "x-request-id", "HTTP_X_REQUEST_ID"
        )
        or str(uuid.uuid4()),
        "remote_addr": request.client.host,
        "path": request.url.path,
        "method": request.method,
    }


class RequestStartMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.time_started = time.time()
        request_body = None
        if settings.ENVIRONMENT in ("stage", "prod"):
            request_body = await request.body()
        logger.info(
            "request_started",
            received_headers=dict(request.headers),
            received_body=request_body,
            query_string=dict(request.query_params),
            **get_vars(request),
        )
        response = await call_next(request)
        return response


class RequestFinishMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        time_started = getattr(request.state, "time_started", None)
        duration = (
            round(time.time() - time_started, 4) if time_started else None
        )
        logger.info(
            "request_finished",
            status=response.status_code,
            request_time=duration,
            sent_headers=dict(response.headers),
            sent_body=getattr(response, "content", None),
            **get_vars(request),
        )
        return response
