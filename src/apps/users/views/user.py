from apps.users.entities.user import UserEntity
from apps.users.services.user import UserService
from fastapi import HTTPException, Response


class UserView:
    def __init__(self):
        self.user_service = UserService()

    async def list(self, response: Response):
        user_entities = await self.user_service.list()
        response.headers["X-Total-Count"] = str(len(user_entities))
        return user_entities

    async def get(self, user_id: int):
        user_entity = await self.user_service.get(user_id)
        if not user_entity:
            raise HTTPException(status_code=404, detail="User not found")
        return user_entity

    async def create(self, user_entity: UserEntity):
        user_entity = await self.user_service.create(user_entity)
        return user_entity

    async def delete(self, user_id: int):
        user_entity = await self.user_service.delete(user_id)
        if not user_entity:
            raise HTTPException(status_code=404, detail="User not found")
        return user_entity
