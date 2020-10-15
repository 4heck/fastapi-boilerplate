from typing import List

from apps.users.entities.user import UserEntity
from apps.users.repositories.user import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def list(self) -> List[UserEntity]:
        user_entities = await self.user_repository.list()
        return user_entities

    async def get(self, user_id: int) -> UserEntity:
        user_entity = await self.user_repository.get(user_id)
        return user_entity

    async def create(self, user_entity: UserEntity) -> UserEntity:
        user_entity = await self.user_repository.create(user_entity)
        return user_entity

    async def delete(self, user_id: int) -> UserEntity:
        user_entity = await self.user_repository.delete(user_id)
        return user_entity
