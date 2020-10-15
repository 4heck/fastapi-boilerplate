import logging
import logging.config

import sentry_sdk
from starlette.datastructures import Secret
from structlog import configure, dev, processors, stdlib
from structlog_sentry import SentryJsonProcessor
from utils.config.base import config
from utils.structlog.base import add_environment, date_formatter

SENTRY_DSN: Secret = config("SENTRY_DSN", cast=Secret)
ENVIRONMENT: str = config("ENVIRONMENT", cast=str)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "required_prod_or_stage": {
            "()": "utils.structlog.base.RequireProdOrStage",
        },
        "required_dev_or_test": {
            "()": "utils.structlog.base.RequiredDevOrTest",
        },
    },
    "formatters": {
        "plain_console": {
            "()": stdlib.ProcessorFormatter,
            "processor": dev.ConsoleRenderer(colors=True),
        },
        "json": {
            "()": stdlib.ProcessorFormatter,
            "processor": processors.JSONRenderer(),
        },
    },
    "handlers": {
        "console_json": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "filters": ["required_prod_or_stage"],
        },
        "console_text": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
            "filters": ["required_dev_or_test"],
        },
    },
    "loggers": {
        "utils": {
            "handlers": ["console_text", "console_json"],
            "level": "INFO",
            "propagate": False,
        },
        "apps.users": {
            "handlers": ["console_text", "console_json"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

logging.config.dictConfig(LOGGING)

dev_processors = [
    stdlib.add_logger_name,
    stdlib.add_log_level,
    processors.StackInfoRenderer(),
    dev.set_exc_info,
    processors.format_exc_info,
    date_formatter,
    add_environment,
    stdlib.ProcessorFormatter.wrap_for_formatter,
]

prod_processors = [
    stdlib.filter_by_level,
    stdlib.add_logger_name,
    stdlib.add_log_level,
    add_environment,
    processors.format_exc_info,
    processors.UnicodeDecoder(),
    processors.TimeStamper(fmt="ISO", utc=True, key="@timestamp"),
    SentryJsonProcessor(level=logging.ERROR, tag_keys=["environment"]),
    stdlib.ProcessorFormatter.wrap_for_formatter,
]

if ENVIRONMENT in ("dev", "test"):
    processors_list = dev_processors
else:
    processors_list = prod_processors
    sentry_sdk.init(
        dsn=str(SENTRY_DSN),
        environment=ENVIRONMENT,
    )


configure(
    processors=processors_list,
    logger_factory=stdlib.LoggerFactory(),
    wrapper_class=stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
