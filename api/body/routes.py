# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:

from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import KartRead
from .services import KartService
from api.bodyTypeGroup.schemas import kartTypeRead

router = APIRouter(
    prefix="/karts",
    tags=["kart"],
)

def get_service(session: SessionDep) -> KartService:
    return KartService(session)
ServiceDep = Annotated[KartService, Depends(get_service)]

@router.get("/", response_model=list[KartRead])
def get_Karts(service: ServiceDep):
    return service.fetch_karts()

@router.get("/{bodyName}", response_model=KartRead)
def get_Kart(service: ServiceDep, bodyName: str):
    return service.fetch_kart(bodyName)

@router.get("/{bodyName}/stats", response_model=kartTypeRead)
def get_kart_stats(service: ServiceDep, bodyName: str):
    return service.fetch_kart_kartType(bodyName)




