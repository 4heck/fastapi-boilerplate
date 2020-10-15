from typing import Optional

from utils.entities.base import BaseEntity


class UserEntity(BaseEntity):
    id: Optional[int] = None
    username: str
