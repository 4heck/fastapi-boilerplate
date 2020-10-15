from core import settings
from structlog import get_logger


logger = get_logger(__name__)


def init_models(app=None):
    for local_app in settings.LOCAL_APPS:
        try:
            __import__(f"{local_app}.models")
        except Exception as exc:
            logger.error("load_models", exc=str(exc))
    return app
