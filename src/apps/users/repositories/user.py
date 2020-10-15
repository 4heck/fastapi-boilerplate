from typing import List

from apps.users.entities.user import UserEntity
from apps.users.models.user import User


class UserRepository:
    async def list(self) -> List[UserEntity]:
        users = await User.query.gino.all()
        return [UserEntity.from_orm(user) for user in users]

    async def get(self, user_id: int) -> UserEntity:
        user = await User.get(user_id)
        if user:
            return UserEntity.from_orm(user)

    async def create(self, user_entity: UserEntity) -> UserEntity:
        user = await User.create(**user_entity.dict(exclude={"id"}))
        if user:
            return UserEntity.from_orm(user)

    async def delete(self, user_id: int) -> None:
        user = await User.get(user_id)
        if user:
            await user.delete()
            return UserEntity.from_orm(user)
