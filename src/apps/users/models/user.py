from core.db import db
from utils.models.base import BaseModelMixin


class User(BaseModelMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.Unicode(), default="noname")
