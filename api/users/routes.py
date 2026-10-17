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

router = APIRouter(
    prefix="/users",
    tags=["user"],
)

def get_service(session: SessionDep) -> UserService:
    return UserService(session)
ServiceDep = Annotated[UserService, Depends(get_service)]

@router.get("/", response_model=list[UserRead])
def get_users(service: ServiceDep):
    return service.fetch_users()

@router.get("/{user_id}", response_model=UserRead)
def get_user(service: ServiceDep, user_id: int):
    return service.fetch_user(user_id)

@router.get("/{user_id}/build", response_model=list[BuildRead])
@router.get("/{user_id}/builds", response_model=list[BuildRead])
def get_user_builds(service: ServiceDep, user_id: int):
    return service.fetch_user_builds(user_id)

@router.get("/{user_id}/builds/{build_id}", response_model=BuildRead)
@router.get("/{user_id}/build/{build_id}", response_model=BuildRead)
def get_user_build(service: ServiceDep, user_id: int, build_id: int):
    return service.fetch_user_build(user_id, build_id)