from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.database import get_session
from .schemas import BuildStatsResponse
from .services import CalculateStatsService

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/calculateStats",
    tags=["calculateStats"]
)

def get_service(session: SessionDep) -> CalculateStatsService:
    return CalculateStatsService(session)

ServiceDep = Annotated[CalculateStatsService, Depends(get_service)]

@router.get("/{driver}/{kart}/{tire}/{glider}", response_model=BuildStatsResponse)
def get_calculated_stats(
    driver: str,
    kart: str,
    tire: str,
    glider: str,
    service: ServiceDep
):
    return service.calculate_build_stats(driver, kart, tire, glider)
