from sentry_sdk import init as initialize_sentry
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from starlette.datastructures import Secret
from utils.config.base import config

SENTRY_DSN: Secret = config("SENTRY_DSN", cast=Secret)
ENVIRONMENT: str = config("ENVIRONMENT", cast=str)

if SENTRY_DSN and ENVIRONMENT in ("stage", "prod"):
    initialize_sentry(
        dsn=str(SENTRY_DSN),
        integrations=[SqlalchemyIntegration()],
        environment=ENVIRONMENT,
    )
