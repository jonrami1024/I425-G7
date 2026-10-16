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
    prefix="/bodies",
    tags=["kart"],
)

def get_service(session: SessionDep) -> KartService:
    return KartService(session)
ServiceDep = Annotated[KartService, Depends(get_service)]

@router.get("/", response_model=list[KartRead])
def get_Karts(service: ServiceDep):
    return service.fetch_karts()

@router.get("/{body_id}", response_model=KartRead)
def get_Kart(service: ServiceDep, body_id: int):
    return service.fetch_kart(body_id)

@router.get("/{body_id}/stats", response_model=kartTypeRead)
def get_kart_stats(service: ServiceDep, body_id: int):
    return service.fetch_kart_kartType(body_id)




