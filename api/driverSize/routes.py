# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep, get_current_user, role_required, AdminDep, UserManagerDep, AdvancedUserDep, BasicUserDep
from .services import DriverGroupService
from .schemas import DriverGroupRead
from api.driver.schemas import DriverRead

router = APIRouter(
    prefix="/driver-groups",
    tags=["Driver Groups"],
    dependencies=[Depends(role_required([1, 2, 3, 4]))]
)

def get_service(session: SessionDep) -> DriverGroupService:
    return DriverGroupService(session)

ServiceDep = Annotated[DriverGroupService, Depends(get_service)]

@router.get("/", response_model=list[DriverGroupRead], summary="Get all driver groups")
def get_driver_size(service: ServiceDep):
    return service.fetch_driverSizes()

@router.get("/{driver_group_id}", response_model=DriverGroupRead, summary="Get one driver group and its stats")
def get_driver_size_group(service: ServiceDep, driver_group_id: int):
    return service.fetch_driverSize(driver_group_id)

@router.get("/{driver_group_id}/drivers", response_model=list[DriverRead], summary="Get all drivers in a driver group")
def get_driver_size_group_drivers(service: ServiceDep, driver_group_id: int):
    return service.fetch_driverSize_drivers(driver_group_id)
