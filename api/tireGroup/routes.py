# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep, get_current_user, role_required, AdminDep, UserManagerDep, AdvancedUserDep, BasicUserDep
from .services import TireGroupService
from .schemas import TireGroupRead
from api.tire.schemas import TireRead

router = APIRouter(
    prefix="/tire-groups",
    tags=["Tire Groups"],
    dependencies=[Depends(role_required([1, 2, 3, 4]))]
)

def get_service(session: SessionDep) -> TireGroupService:
    return TireGroupService(session)

ServiceDep = Annotated[TireGroupService, Depends(get_service)]

@router.get("/", response_model=list[TireGroupRead], summary="Get all tire groups")
def get_tire_groups(service: ServiceDep):
    return service.fetch_tireGroups()

@router.get("/{tire_group_id}", response_model=TireGroupRead, summary="Get one tire group and its stats")
def get_tire_groups_stats(service: ServiceDep, tire_group_id: int):
    return service.fetch_tireGroup(tire_group_id)

@router.get("/{tire_group_id}/tires", response_model=list[TireRead], summary="Get all tires in a tire group")
def get_tire_groups_tires(service: ServiceDep, tire_group_id: int):
    return service.fetch_tireGroups_tires(tire_group_id)
