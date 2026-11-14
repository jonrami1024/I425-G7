# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends, Query
from typing import Annotated, Union, Optional
from api.dependencies import SessionDep, get_current_user, role_required, AdminDep, UserManagerDep, AdvancedUserDep, BasicUserDep
from .schemas import UserRead, UserPage, UserCreate, UserUpdate, DeleteResponse
from .services import UserService
from api.builds.schemas import BuildRead
from api.build_ratings.schemas import RatingRead

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(role_required([1,2]))]
)

def get_service(session: SessionDep) -> UserService:
    return UserService(session)
ServiceDep = Annotated[UserService, Depends(get_service)]

@router.get("/", response_model=Union[list[UserRead], UserPage], summary="Get all users")
def get_users(service: ServiceDep,
              limit: Optional[int] = Query(default=None, ge=1),
              offset: Optional[int] = Query(default=0, ge=0),
              sort: Optional[str] = Query(default=None)
              ):
    return service.fetch_users(limit=limit, offset=offset, sort=sort)

@router.get("/search", response_model=list[UserRead], summary="Search Users")
def search_users(service: ServiceDep,
                 q: Optional[str] = Query(default=None),
                 logic: str = Query(default="or")):
    return service.search_users(q, logic)

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

@router.post("/", response_model=UserRead, status_code=201, summary="Create a user")
def create_user(service: ServiceDep, user_data: UserCreate):
    return service.create_user(user_data)

@router.put("/{user_id}", response_model=UserRead, summary="Update a user")
def update_user(service: ServiceDep, user_id: int, user_data: UserUpdate):
    return service.update_user(user_id, user_data)

@router.delete("/{user_id}", response_model=DeleteResponse, summary="Delete a user and their builds and ratings")
def delete_user(service: ServiceDep, user_id: int):
    return service.delete_user(user_id)
