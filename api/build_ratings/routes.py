# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:
from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import RatingRead
from .services import RatingsService


router = APIRouter(
    prefix="/ratings",
    tags=["rating"],
)

def get_service(session: SessionDep) -> RatingsService:
    return RatingsService(session)
ServiceDep = Annotated[RatingsService, Depends(get_service)]

@router.get("/", response_model=list[RatingRead])
def get_ratings(service: ServiceDep):
    return service.fetch_ratings()

@router.get("/{rating_id}", response_model=RatingRead)
def get_rating(service: ServiceDep, rating_id: int):
    return service.fetch_rating(rating_id)