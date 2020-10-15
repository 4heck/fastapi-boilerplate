from typing import Type

from core.db import db
from gino.declarative import declared_attr  # type: ignore
from pydantic import BaseConfig, BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic  # type: ignore


class PydanticConfig(BaseConfig):
    orm_mode = True


class BaseModelMixin:
    _model = None
    readable_field = "id"

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()  # type: ignore

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=db.func.now(),
        onupdate=db.func.now(),
    )

    @classmethod
    def model(cls) -> Type[BaseModel]:
        if not cls._model:
            cls._model = sqlalchemy_to_pydantic(
                cls, config=PydanticConfig, exclude=["id"]
            )
        return cls._model

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {getattr(self, self.readable_field)}>"
