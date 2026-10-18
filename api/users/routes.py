# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import UserRead
from .services import UserService
from api.builds.schemas import BuildRead
from api.build_ratings.schemas import RatingRead

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

def get_service(session: SessionDep) -> UserService:
    return UserService(session)
ServiceDep = Annotated[UserService, Depends(get_service)]

@router.get("/", response_model=list[UserRead], summary="Get all users")
def get_users(service: ServiceDep):
    return service.fetch_users()

@router.get("/{user_id}", response_model=UserRead, summary="Get one user")
def get_user(service: ServiceDep, user_id: int):
    return service.fetch_user(user_id)

@router.get("/{user_id}/builds", response_model=list[BuildRead], summary="Get all builds saved by a user")
def get_user_builds(service: ServiceDep, user_id: int):
    return service.fetch_user_builds(user_id)

@router.get("/{user_id}/builds/{build_id}", response_model=BuildRead, summary="Get one of a user's builds")
def get_user_build(service: ServiceDep, user_id: int, build_id: int):
    return service.fetch_user_build(user_id, build_id)

@router.get("/{user_id}/ratings", response_model=list[RatingRead], summary="Get all ratings a user has given")
def get_user_ratings(service: ServiceDep, user_id: int):
    return service.fetch_user_ratings(user_id)
