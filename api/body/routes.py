# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import BodyRead
from .services import BodyService
from api.bodyTypeGroup.schemas import BodyGroupRead
from api.builds.schemas import BuildRead

router = APIRouter(
    prefix="/bodies",
    tags=["Bodies"],
)

def get_service(session: SessionDep) -> BodyService:
    return BodyService(session)
ServiceDep = Annotated[BodyService, Depends(get_service)]

@router.get("/", response_model=list[BodyRead], summary="Get all bodies")
def get_Karts(service: ServiceDep):
    return service.fetch_karts()

@router.get("/{body_id}", response_model=BodyRead, summary="Get one body")
def get_Kart(service: ServiceDep, body_id: int):
    return service.fetch_kart(body_id)

@router.get("/{body_id}/stats", response_model=BodyGroupRead, summary="Get a body's stats (its body group)")
def get_kart_stats(service: ServiceDep, body_id: int):
    return service.fetch_kart_kartType(body_id)

@router.get("/{body_id}/builds", response_model=list[BuildRead], summary="Get all builds that use a body")
def get_kart_builds(service: ServiceDep, body_id: int):
    return service.fetch_kart_builds(body_id)
