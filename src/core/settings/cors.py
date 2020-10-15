from utils.config.base import config

CORS_ORIGINS: list = config(
    "CORS_ORIGINS",
    cast=list,
    default=["*"],
)
CORS_ALLOW_METHODS: list = config(
    "CORS_ALLOW_METHODS",
    cast=list,
    default=["*"],
)
CORS_ALLOW_HEADERS: list = config(
    "CORS_ALLOW_HEADERS",
    cast=list,
    default=["*"],
)
CORS_ALLOW_CREDENTIALS: bool = config(
    "CORS_ALLOW_CREDENTIALS",
    cast=bool,
    default=True,
)
CORS_EXPOSE_HEADERS: list = config(
    "CORS_EXPOSE_HEADERS",
    cast=list,
    default=["X-Total-Count"],
)
