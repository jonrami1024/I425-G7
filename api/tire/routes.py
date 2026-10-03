# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: routes.py
# Description:
from fastapi import APIRouter, Depends
from typing import Annotated
from api.dependencies import SessionDep
from .schemas import TireRead
from .services import TireService
from api.tireGroup.schemas import tireGroupRead

router = APIRouter(
    prefix="/tires",
    tags=["tire"],
)

def get_service(session: SessionDep) -> TireService:
    return TireService(session)

ServiceDep = Annotated[TireService, Depends(get_service)]

@router.get("/", response_model=list[TireRead])
def get_tires(service:ServiceDep):
    return service.fetch_tires()

@router.get("/{tire}", response_model=TireRead)
def get_tire(service: ServiceDep, tire:str):
    return service.fetch_tire(tire)

@router.get("/{tire}/stats", response_model=tireGroupRead)
def get_tire_stats(service: ServiceDep, tire:str):
    return service.fetch_tire_tireGroup(tire)

