# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:
from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import BuildRead
from .services import BuildService
from api.calculateStats.schemas import BuildStatsResponse
from api.build_ratings.schemas import RatingRead

router = APIRouter(
    prefix="/builds",
    tags=["build"],
)

def get_service(session: SessionDep) -> BuildService:
    return BuildService(session)
ServiceDep = Annotated[BuildService, Depends(get_service)]

@router.get("/", response_model=list[BuildRead])
def get_builds(service: ServiceDep):
    return service.fetch_builds()

@router.get("/{build_id}", response_model=BuildRead)
def get_build(service: ServiceDep, build_id: int):
    return service.fetch_build(build_id)

@router.get("/{build_id}/stats", response_model=BuildStatsResponse)
def get_build_stats(service: ServiceDep, build_id: int):
    return service.fetch_build_stats(build_id)

@router.get("/{build_id}/ratings", response_model=list[RatingRead])
def get_build_ratings(service: ServiceDep, build_id: int):
    return service.fetch_build_ratings(build_id)

@router.get("/{build_id}/ratings/{rating_id}", response_model=RatingRead)
def get_build_rating(service: ServiceDep, build_id: int, rating_id: int):
    return service.fetch_build_rating(build_id, rating_id)
