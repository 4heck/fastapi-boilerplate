from fastapi import FastAPI
from utils.db.base import db

from core.middlewares import init_middlewares
from core.routers import init_routers


def get_app():
    app: FastAPI = FastAPI()
    init_middlewares(app)
    db.init_app(app)
    init_routers(app)
    return app
