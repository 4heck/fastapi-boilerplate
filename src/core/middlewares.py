from core import settings
from starlette.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from utils.middlewares.structlog import (
    RequestFinishMiddleware,
    RequestStartMiddleware,
)


middleware = [
    Middleware(RequestStartMiddleware),  # should be first
    Middleware(SentryAsgiMiddleware),
    Middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
        expose_headers=settings.CORS_EXPOSE_HEADERS,
    ),
    Middleware(RequestFinishMiddleware),  # should be last
]
