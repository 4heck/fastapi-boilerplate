from core import settings
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from utils.middlewares.structlog import (
    RequestFinishMiddleware,
    RequestStartMiddleware,
)


def init_middlewares(app):
    app.add_middleware(RequestStartMiddleware)  # should be first
    app.add_middleware(SentryAsgiMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
        expose_headers=settings.CORS_EXPOSE_HEADERS,
    )
    app.add_middleware(RequestFinishMiddleware)  # should be last
    return app
