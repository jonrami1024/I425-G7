# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .services import KartTypeService
from .schemas import kartTypeRead
from api.body.schemas import KartRead

router = APIRouter(
    prefix="/body-groups",
    tags=["Body Groups"]
)

def get_service(session: SessionDep) -> KartTypeService:
    return KartTypeService(session)

ServiceDep = Annotated[KartTypeService, Depends(get_service)]

@router.get("/", response_model=list[kartTypeRead], summary="Get all body groups")
def get_kart_Type(service: ServiceDep):
    return service.fetch_kartTypes()

@router.get("/{body_group_id}", response_model=kartTypeRead, summary="Get one body group and its stats")
def get_kart_Type_group(service: ServiceDep, body_group_id: int):
    return service.fetch_kartType(body_group_id)

@router.get("/{body_group_id}/bodies", response_model=list[KartRead], summary="Get all bodies in a body group")
def get_kartType_karts(service: ServiceDep, body_group_id: int):
    return service.fetch_kartType_karts(body_group_id)
