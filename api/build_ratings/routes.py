# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends, Query
from typing import Annotated, Union, Optional
from api.dependencies import SessionDep
from .schemas import RatingRead, RatingPage
from .services import RatingsService


router = APIRouter(
    prefix="/ratings",
    tags=["Ratings"],
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
