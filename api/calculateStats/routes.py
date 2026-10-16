from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.database import get_session
from .schemas import BuildStatsResponse
from .services import CalculateStatsService

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(
    prefix="/combinations",
    tags=["calculateStats"]
)

def get_service(session: SessionDep) -> CalculateStatsService:
    return CalculateStatsService(session)

ServiceDep = Annotated[CalculateStatsService, Depends(get_service)]

@router.get("/", response_model=BuildStatsResponse)
def get_calculated_stats(
    driver_id: int,
    body_id: int,
    tire_id: int,
    glider_id: int,
    service: ServiceDep
):
    return service.calculate_build_stats(driver_id, body_id, tire_id, glider_id)

