# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .services import DriverSizeService
from .schemas import driverSizeRead
from api.driver.schemas import DriverRead

router = APIRouter(
    prefix="/stats",
    tags=["driver stats"]
)

def get_service(session: SessionDep) -> DriverSizeService:
    return DriverSizeService(session)

ServiceDep = Annotated[DriverSizeService, Depends(get_service)]

@router.get("/", response_model=list[driverSizeRead])
def get_driver_size(service: ServiceDep):
    return service.fetch_driverSizes()

@router.get("/{stats}", response_model=driverSizeRead)
def get_driver_size_group(service: ServiceDep, driverSizeGroup: str):
    return service.fetch_driverSize(driverSizeGroup)

@router.get("/{stats}/drivers", response_model=list[DriverRead])
def get_driver_size_group_drivers(service: ServiceDep, driverSizeGroup: str):
    return service.fetch_driverSize_drivers(driverSizeGroup)
