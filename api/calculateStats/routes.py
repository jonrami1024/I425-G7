from typing import Annotated
from fastapi import APIRouter, Depends
from api.dependencies import SessionDep
from .schemas import CombinationRead
from .services import CalculateStatsService

router = APIRouter(
    prefix="/combinations",
    tags=["Combinations"]
)

def get_service(session: SessionDep) -> CalculateStatsService:
    return CalculateStatsService(session)

ServiceDep = Annotated[CalculateStatsService, Depends(get_service)]

@router.get("/", response_model=CombinationRead, summary="Calculate the stats for any combination of parts")
def get_calculated_stats(
    driver_id: int,
    body_id: int,
    tire_id: int,
    glider_id: int,
    service: ServiceDep
):
    return service.calculate_build_stats(driver_id, body_id, tire_id, glider_id)
