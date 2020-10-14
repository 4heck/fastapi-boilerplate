from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from utils.middlewares.structlog import (
    RequestFinishMiddleware,
    RequestStartMiddleware,
)


def init_middlewares(app):
    app.add_middleware(SentryAsgiMiddleware)
    app.add_middleware(RequestStartMiddleware)
    app.add_middleware(RequestFinishMiddleware)
    return app
