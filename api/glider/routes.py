# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import GliderRead
from .services import GliderService
from api.builds.schemas import BuildRead

router = APIRouter(
    prefix="/gliders",
    tags=["Gliders"],
)

def get_service(session: SessionDep) -> GliderService:
    return GliderService(session)

ServiceDep = Annotated[GliderService, Depends(get_service)]

@router.get("/", response_model=list[GliderRead], summary="Get all gliders and their stats")
def get_gliders(service: ServiceDep):
    return service.fetch_gliders()

@router.get("/{glider_id}", response_model=GliderRead, summary="Get one glider and its stats")
def get_glider(service: ServiceDep, glider_id: int):
    return service.fetch_glider(glider_id)

@router.get("/{glider_id}/builds", response_model=list[BuildRead], summary="Get all builds that use a glider")
def get_glider_builds(service: ServiceDep, glider_id: int):
    return service.fetch_glider_builds(glider_id)
