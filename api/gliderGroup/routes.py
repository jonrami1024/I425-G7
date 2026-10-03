# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .services import GliderGroupService
from .schemas import gliderGroupRead
from api.glider.schemas import GliderRead

router = APIRouter(
    prefix="/gliderStats",
    tags=["glider stats"],
)

def get_service(session: SessionDep) -> GliderGroupService:
    return GliderGroupService(session)

ServiceDep = Annotated[GliderGroupService, Depends(get_service)]

@router.get("/", response_model=list[gliderGroupRead])
def get_glider_groups(service: ServiceDep):
    return service.fetch_gliderGroups()

@router.get("/{stats}", response_model=gliderGroupRead)
def get_glider_groups_stats(service: ServiceDep, stats: str):
    return service.fetch_gliderGroup(stats)

@router.get("/{stats}/gliders", response_model=list[GliderRead])
def get_glider_groups_gliders(service: ServiceDep, stats: str):
    return service.fetch_gliderGroup_gliders(stats)