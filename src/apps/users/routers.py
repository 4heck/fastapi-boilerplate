from typing import List

from apps.users.entities.user import UserEntity
from apps.users.views.user import UserView
from fastapi import APIRouter

router = APIRouter()
user_view = UserView()

router.get(
    "/",
    name="list",
    summary="List users",
    response_model=List[UserEntity],
)(user_view.list)

router.get(
    "/{user_id}",
    name="get",
    summary="Get user by id",
    response_model=UserEntity,
)(user_view.get)

router.post(
    "/",
    name="create",
    summary="Create user",
    response_model=UserEntity,
)(user_view.create)

router.delete(
    "/{user_id}",
    name="delete",
    summary="Delete user",
    response_model=UserEntity,
)(user_view.delete)
