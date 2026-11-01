# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends, Query
from typing import Annotated, Union, Optional
from api.dependencies import SessionDep
from .schemas import BuildRead, BuildPage, BuildCreate, BuildUpdate
from .services import BuildService
from api.calculateStats.schemas import BuildStatsRead
from api.build_ratings.schemas import RatingRead
from api.users.schemas import UserRead, DeleteResponse
from api.driver.schemas import DriverRead
from api.body.schemas import BodyRead
from api.tire.schemas import TireRead
from api.glider.schemas import GliderRead

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

@router.get("/search", response_model=list[BuildRead], summary="Search builds")
def search_builds(service: ServiceDep,
                  q: Optional[str] = Query(default=None),
                  logic: str = Query(default="or")):
    return service.search_builds(q, logic)

@router.get("/{build_id}", response_model=BuildRead, summary="Get one build")
def get_build(service: ServiceDep, build_id: int):
    return service.fetch_build(build_id)

@router.get("/{build_id}/user", response_model=UserRead, summary="Get the user who saved a build")
def get_build_user(service: ServiceDep, build_id: int):
    return service.fetch_build_user(build_id)

@router.get("/{build_id}/driver", response_model=DriverRead, summary="Get a build's driver")
def get_build_driver(service: ServiceDep, build_id: int):
    return service.fetch_build_driver(build_id)

@router.get("/{build_id}/body", response_model=BodyRead, summary="Get a build's body")
def get_build_body(service: ServiceDep, build_id: int):
    return service.fetch_build_body(build_id)

@router.get("/{build_id}/tire", response_model=TireRead, summary="Get a build's tire")
def get_build_tire(service: ServiceDep, build_id: int):
    return service.fetch_build_tire(build_id)

@router.get("/{build_id}/glider", response_model=GliderRead, summary="Get a build's glider")
def get_build_glider(service: ServiceDep, build_id: int):
    return service.fetch_build_glider(build_id)

@router.get("/{build_id}/stats", response_model=BuildStatsRead, summary="Get the combined stats of a build")
def get_build_stats(service: ServiceDep, build_id: int):
    return service.fetch_build_stats(build_id)

@router.get("/{build_id}/ratings", response_model=list[RatingRead], summary="Get all ratings for a build")
def get_build_ratings(service: ServiceDep, build_id: int):
    return service.fetch_build_ratings(build_id)

@router.get("/{build_id}/ratings/{rating_id}", response_model=RatingRead, summary="Get one rating for a build")
def get_build_rating(service: ServiceDep, build_id: int, rating_id: int):
    return service.fetch_build_rating(build_id, rating_id)

@router.post("/", response_model=BuildRead, status_code=201, summary="Create a build")
def create_build(service: ServiceDep, build_data: BuildCreate):
    return service.create_build(build_data)

@router.put("/{build_id}", response_model=BuildRead, summary="Update a build")
def update_build(service: ServiceDep, build_id: int, build_data: BuildUpdate):
    return service.update_build(build_id, build_data)

@router.delete("/{build_id}", response_model=DeleteResponse, summary="Delete a build and its ratings")
def delete_build(service: ServiceDep, build_id: int):
    return service.delete_build(build_id)
