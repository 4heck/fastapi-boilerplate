from utils.entities.base import BaseEntity


class UserEntity(BaseEntity):
    username: str
    password: str
