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

router = APIRouter(
    prefix="/drivers",
    tags=["driver"]
)

def get_service(session: SessionDep) -> DriverService:
    return DriverService(session)

ServiceDep = Annotated[DriverService, Depends(get_service)]

@router.get("/", response_model=list[DriverRead])
def get_drivers(service:ServiceDep):
    return service.fetch_drivers()

@router.get("/{driver_id}", response_model=DriverRead)
def get_driver(service: ServiceDep, driver_id: int):
    return service.fetch_driver(driver_id)

@router.get("/{driver_id}/stats", response_model=driverSizeRead)
def get_driver_size(service: ServiceDep, driver_id: int):
    return service.fetch_driver_driverSize(driver_id)