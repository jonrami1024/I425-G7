# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import DriverRead
from .services import DriverService
from api.driverSize.schemas import driverSizeRead
from api.builds.schemas import BuildRead

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"]
)

def get_service(session: SessionDep) -> DriverService:
    return DriverService(session)

ServiceDep = Annotated[DriverService, Depends(get_service)]

@router.get("/", response_model=list[DriverRead], summary="Get all drivers")
def get_drivers(service: ServiceDep):
    return service.fetch_drivers()

@router.get("/{driver_id}", response_model=DriverRead, summary="Get one driver")
def get_driver(service: ServiceDep, driver_id: int):
    return service.fetch_driver(driver_id)

@router.get("/{driver_id}/stats", response_model=driverSizeRead, summary="Get a driver's stats (its driver group)")
def get_driver_size(service: ServiceDep, driver_id: int):
    return service.fetch_driver_driverSize(driver_id)

@router.get("/{driver_id}/builds", response_model=list[BuildRead], summary="Get all builds that use a driver")
def get_driver_builds(service: ServiceDep, driver_id: int):
    return service.fetch_driver_builds(driver_id)
