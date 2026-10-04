from sqlmodel import Session
from fastapi import HTTPException
from api.driver.models import Drivers
from api.body.models import Karts
from api.tire.models import Tires
from api.glider.models import Gliders
from api.calculateStats.schemas import BuildStatsResponse, StatDetail

class CalculateStatsService:
    def __init__(self, session: Session):
        self.session = session

    def calculate_build_stats(self, driver_name: str, kart_name: str, tire_name: str, glider_name: str) -> BuildStatsResponse:
        driver = self.session.get(Drivers, driver_name)
        if not driver or not driver.driverSize:
            raise HTTPException(status_code=404, detail=f"Driver not found")

        kart = self.session.get(Karts, kart_name)
        if not kart or not kart.kartType:
            raise HTTPException(status_code=404, detail=f"Kart not found")

        tire = self.session.get(Tires, tire_name)
        if not tire or not tire.tire_group:
            raise HTTPException(status_code=404, detail=f"Tire not found")

        glider = self.session.get(Gliders, glider_name)
        if not glider or not glider.glider_group:
            raise HTTPException(status_code=404, detail=f"Glider not found")

        d_stat = driver.driverSize
        k_stat = kart.kartType
        t_stat = tire.tire_group
        g_stat = glider.glider_group

        speed_level = d_stat.speed + k_stat.speed + t_stat.speed + g_stat.speed
        accel_level = d_stat.acceleration + k_stat.acceleration + t_stat.acceleration + g_stat.acceleration
        weight_level = d_stat.weight + k_stat.weight + t_stat.weight + g_stat.weight
        handling_level = d_stat.handling + k_stat.handling + t_stat.handling + g_stat.handling
        miniturbo_level = d_stat.miniTurbo + k_stat.miniTurbo + t_stat.miniTurbo + g_stat.miniTurbo
        invincibility_level = d_stat.invincibility + k_stat.invincibility + t_stat.invincibility + g_stat.invincibility

        return BuildStatsResponse(
            driver=driver_name,
            kart=kart_name,
            tire=tire_name,
            glider=glider_name,
            speed=StatDetail(level=speed_level, value=(speed_level + 3) / 4.0),
            acceleration=StatDetail(level=accel_level, value=(accel_level + 3) / 4.0),
            weight=StatDetail(level=weight_level, value=(weight_level + 3) / 4.0),
            handling=StatDetail(level=handling_level, value=(handling_level + 3) / 4.0),
            miniTurbo=StatDetail(level=miniturbo_level, value=(miniturbo_level + 3) / 4.0),
            invincibility=StatDetail(level=invincibility_level, value=(invincibility_level + 3) / 4.0)
        )
