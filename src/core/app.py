from core.db import db
from core.middlewares import init_middlewares
from core.models import init_models
from core.routers import init_routers
from fastapi import FastAPI


def get_app():
    app: FastAPI = FastAPI()
    db.init_app(app)
    init_middlewares(app)
    init_routers(app)
    init_models(app)
    return app
