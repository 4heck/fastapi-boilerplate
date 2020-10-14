import structlog
from starlette.requests import Request
from starlette.responses import Response

structlog.configure(processors=[structlog.processors.JSONRenderer()])
logger = structlog.get_logger()


async def logging_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    log = logger.bind(
        url=str(request.url),
        method=request.method,
    )
    try:
        response: Response = await call_next(request)
    finally:
        log.msg(
            status=response.status_code,
        )
    return response
