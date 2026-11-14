# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends, Query
from typing import Annotated, Union, Optional
from api.dependencies import SessionDep, get_current_user, role_required, AdminDep, UserManagerDep, AdvancedUserDep, BasicUserDep
from .schemas import RatingRead, RatingPage, RatingCreate, RatingUpdate
from .services import RatingsService
from api.builds.schemas import BuildRead
from api.users.schemas import UserRead, DeleteResponse


router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"],
    dependencies=[Depends(role_required([1, 2, 3, 4]))]
)

def get_service(session: SessionDep) -> RatingsService:
    return RatingsService(session)
ServiceDep = Annotated[RatingsService, Depends(get_service)]

@router.get("/", response_model=Union[list[RatingRead], RatingPage], summary="Get all ratings")
def get_ratings(service: ServiceDep,
                limit: Optional[int] = Query(default=None, ge=1),
                offset: Optional[int] = Query(default=0, ge=0),
                sort: Optional[str] = Query(default=None)
                ):
    return service.fetch_ratings(limit=limit, offset=offset, sort=sort)

@router.get("/{rating_id}", response_model=RatingRead, summary="Get one rating")
def get_rating(service: ServiceDep, rating_id: int):
    return service.fetch_rating(rating_id)

@router.get("/{rating_id}/build", response_model=BuildRead, summary="Get the build a rating is for")
def get_rating_build(service: ServiceDep, rating_id: int):
    return service.fetch_rating_build(rating_id)

@router.get("/{rating_id}/user", response_model=UserRead, summary="Get the user who gave a rating")
def get_rating_user(service: ServiceDep, rating_id: int):
    return service.fetch_rating_user(rating_id)

@router.post("/", response_model=RatingRead, status_code=201, summary="Rate a build")
def create_rating(service: ServiceDep, rating_data: RatingCreate, _user: AdvancedUserDep):
    return service.create_rating(rating_data)

@router.put("/{rating_id}", response_model=RatingRead, summary="Update a rating")
def update_rating(service: ServiceDep, rating_id: int, rating_data: RatingUpdate, _user: AdvancedUserDep):
    return service.update_rating(rating_id, rating_data)

@router.delete("/{rating_id}", response_model=DeleteResponse, summary="Delete a rating")
def delete_rating(service: ServiceDep, rating_id: int, _user: AdvancedUserDep):
    return service.delete_rating(rating_id)
