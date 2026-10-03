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
    prefix="/kartStats",
    tags=["kart stats"]
)

def get_service(session: SessionDep) -> KartTypeService:
    return KartTypeService(session)

ServiceDep = Annotated[KartTypeService, Depends(get_service)]

@router.get("/", response_model=list[kartTypeRead])
def get_kart_Type(service: ServiceDep):
    return service.fetch_kartTypes()

@router.get("/{stats}", response_model=kartTypeRead)
def get_kart_Type_group(service: ServiceDep, bodyTypeGroup: str):
    return service.fetch_kartType(bodyTypeGroup)

@router.get("/{stats}/karts", response_model=list[KartRead])
def get_kartType_karts(service: ServiceDep, bodyTypeGroup: str):
    return service.fetch_kartType_karts(bodyTypeGroup)