from sqlmodel import Session
from fastapi import HTTPException
from api.driver.models import Drivers
from api.body.models import Karts
from api.tire.models import Tires
from api.glider.models import Gliders
from api.calculateStats.schemas import CombinationRead, StatsBlock, StatDetail

STATS = ["speed", "acceleration", "weight", "handling", "traction", "mini_turbo", "invincibility"]

class CalculateStatsService:
    def __init__(self, session: Session):
        self.session = session

    def calculate_build_stats(self, driver_id: int, body_id: int, tire_id: int, glider_id: int) -> CombinationRead:
        driver = self.session.get(Drivers, driver_id)
        if not driver or not driver.driverSize:
            raise HTTPException(status_code=404, detail="Driver not found")

        body = self.session.get(Karts, body_id)
        if not body or not body.kartType:
            raise HTTPException(status_code=404, detail="Body not found")

        tire = self.session.get(Tires, tire_id)
        if not tire or not tire.tire_group:
            raise HTTPException(status_code=404, detail="Tire not found")

        glider = self.session.get(Gliders, glider_id)
        if not glider:
            raise HTTPException(status_code=404, detail="Glider not found")

        parts = [driver.driverSize, body.kartType, tire.tire_group, glider]
        stats = {}
        for stat in STATS:
            level = sum(getattr(part, stat) for part in parts)
            stats[stat] = StatDetail(level=level, value=(level + 3) / 4.0)

        return CombinationRead(
            driver=driver.name,
            body=body.name,
            tire=tire.name,
            glider=glider.name,
            stats=StatsBlock(**stats)
        )
