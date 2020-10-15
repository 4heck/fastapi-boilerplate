import logging
import os
import socket
from datetime import date, datetime
from multiprocessing import current_process

from core import settings


def add_environment(_, __, event_dict):
    event_dict["@version"] = 1
    event_dict["environment"] = settings.ENVIRONMENT
    event_dict["hostname"] = socket.gethostname()
    event_dict["proc_pid"] = os.getpid()
    event_dict["proc_index"] = current_process._identity[0]

    return event_dict


def date_formatter(_, __, event_dict):
    for key in event_dict.keys():
        if isinstance(event_dict[key], (date, datetime)):
            event_dict[key] = str(event_dict[key])
    return event_dict


class RequireProdOrStage(logging.Filter):
    def filter(self, record):
        return settings.ENVIRONMENT in ("prod", "stage")


class RequiredDevOrTest(logging.Filter):
    def filter(self, record):
        return settings.ENVIRONMENT in ("dev", "test")
