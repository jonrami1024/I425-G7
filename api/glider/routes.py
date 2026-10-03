# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:
from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import GliderRead
from .services import GliderService
from api.gliderGroup.schemas import gliderGroupRead

router = APIRouter(
    prefix="/gliders",
    tags=["glider"],
)

def get_service(session: SessionDep) -> GliderService:
    return GliderService(session)

ServiceDep = Annotated[GliderService, Depends(get_service)]

@router.get("/", response_model=list[GliderRead])
def get_gliders(service: ServiceDep):
    return service.fetch_gliders()

@router.get("/{glider}", response_model=GliderRead)
def get_glider(service: ServiceDep, glider: str):
    return service.fetch_glider(glider)

@router.get("/{glider}/stats", response_model=gliderGroupRead)
def get_glider_group(service: ServiceDep, glider: str):
    return service.fetch_glider_gliderGroup(glider)
