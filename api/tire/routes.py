# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import TireRead
from .services import TireService
from api.tireGroup.schemas import tireGroupRead
from api.builds.schemas import BuildRead

router = APIRouter(
    prefix="/tires",
    tags=["Tires"],
)

def get_service(session: SessionDep) -> TireService:
    return TireService(session)

ServiceDep = Annotated[TireService, Depends(get_service)]

@router.get("/", response_model=list[TireRead], summary="Get all tires")
def get_tires(service: ServiceDep):
    return service.fetch_tires()

@router.get("/{tire_id}", response_model=TireRead, summary="Get one tire")
def get_tire(service: ServiceDep, tire_id: int):
    return service.fetch_tire(tire_id)

@router.get("/{tire_id}/stats", response_model=tireGroupRead, summary="Get a tire's stats (its tire group)")
def get_tire_stats(service: ServiceDep, tire_id: int):
    return service.fetch_tire_tireGroup(tire_id)

@router.get("/{tire_id}/builds", response_model=list[BuildRead], summary="Get all builds that use a tire")
def get_tire_builds(service: ServiceDep, tire_id: int):
    return service.fetch_tire_builds(tire_id)
