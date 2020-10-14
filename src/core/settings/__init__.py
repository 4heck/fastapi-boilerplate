from typing import List

from utils.config.base import config

ENVIRONMENT: str = config("ENVIRONMENT", cast=str)
LOCAL_APPS: List[str] = ["apps.users"]

from core.settings.db import *  # noqa
from core.settings.logging import *  # noqa
from core.settings.monitoring import *  # noqa
