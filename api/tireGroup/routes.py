# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:
from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .services import TireGroupService
from .schemas import tireGroupRead
from api.tire.schemas import TireRead

router = APIRouter(
    prefix="/tireStats",
    tags=["tire stats"],
)

def get_service(session: SessionDep) -> TireGroupService:
    return TireGroupService(session)

ServiceDep = Annotated[TireGroupService, Depends(get_service)]

@router.get("/", response_model=list[tireGroupRead])
def get_tire_groups(service: ServiceDep):
    return service.fetch_tireGroups()

@router.get("/{stats}", response_model=tireGroupRead)
def get_tire_groups_stats(service: ServiceDep, stats: str):
    return service.fetch_tireGroup(stats)

@router.get("/{stats}/tires", response_model=list[TireRead])
def get_tire_groups_tires(service: ServiceDep, stats: str):
    return service.fetch_tireGroups_tires(stats)