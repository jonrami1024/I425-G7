# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends, Query
from typing import Annotated, Union, Optional
from api.dependencies import SessionDep
from .schemas import BuildRead, BuildPage
from .services import BuildService
from api.calculateStats.schemas import BuildStatsRead
from api.build_ratings.schemas import RatingRead

router = APIRouter(
    prefix="/builds",
    tags=["Builds"],
)

def get_service(session: SessionDep) -> BuildService:
    return BuildService(session)
ServiceDep = Annotated[BuildService, Depends(get_service)]

@router.get("/", response_model=Union[list[BuildRead], BuildPage], summary="Get all builds from all users")
def get_builds(service: ServiceDep,
               limit: Optional[int] = Query(default=None, ge=1),
               offset: Optional[int] = Query(default=0, ge=0),
               sort: Optional[str] = Query(default=None)
               ):
    return service.fetch_builds(limit=limit, offset=offset, sort=sort)

@router.get("/{build_id}", response_model=BuildRead, summary="Get one build")
def get_build(service: ServiceDep, build_id: int):
    return service.fetch_build(build_id)

@router.get("/{build_id}/stats", response_model=BuildStatsRead, summary="Get the combined stats of a build")
def get_build_stats(service: ServiceDep, build_id: int):
    return service.fetch_build_stats(build_id)

@router.get("/{build_id}/ratings", response_model=list[RatingRead], summary="Get all ratings for a build")
def get_build_ratings(service: ServiceDep, build_id: int):
    return service.fetch_build_ratings(build_id)

@router.get("/{build_id}/ratings/{rating_id}", response_model=RatingRead, summary="Get one rating for a build")
def get_build_rating(service: ServiceDep, build_id: int, rating_id: int):
    return service.fetch_build_rating(build_id, rating_id)
