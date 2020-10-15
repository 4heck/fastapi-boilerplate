from typing import Any, Optional

from sqlalchemy.engine.url import make_url, URL
from starlette.datastructures import Secret
from utils.config.base import config

DB_DRIVER: str = config("DB_DRIVER", cast=str, default="postgresql")
DB_HOST: str = config("DB_HOST", cast=str)
DB_PORT: int = config("DB_PORT", cast=int)
DB_USER: str = config("DB_USER", cast=str)
DB_PASSWORD: Secret = config("DB_PASSWORD", cast=Secret)
DB_DATABASE: str = config("DB_DATABASE", cast=str)
DB_DSN: URL = config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)
DB_POOL_MIN_SIZE: int = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE: int = config("DB_POOL_MAX_SIZE", cast=int, default=16)
DB_ECHO: Optional[bool] = config("DB_ECHO", cast=bool, default=False)
DB_SSL: Optional[Any] = config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST: bool = config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
)
DB_RETRY_LIMIT: int = config("DB_RETRY_LIMIT", cast=int, default=5)
DB_RETRY_INTERVAL: int = config("DB_RETRY_INTERVAL", cast=int, default=1)
