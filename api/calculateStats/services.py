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

    def calculate_build_stats(self, driver_id: int, body_id: int, tire_id: str, glider_id: int) -> BuildStatsResponse:
        driver = self.session.get(Drivers, driver_id)
        if not driver or not driver.driverSize:
            raise HTTPException(status_code=404, detail=f"Driver not found")

        kart = self.session.get(Karts, body_id)
        if not kart or not kart.kartType:
            raise HTTPException(status_code=404, detail=f"Kart not found")

        tire = self.session.get(Tires, tire_id)
        if not tire or not tire.tire_group:
            raise HTTPException(status_code=404, detail=f"Tire not found")

        glider = self.session.get(Gliders, glider_id)
        if not glider or not glider.glider_group:
            raise HTTPException(status_code=404, detail=f"Glider not found")

        d_stat = driver.driverSize
        k_stat = kart.kartType
        t_stat = tire.tire_group
        g_stat = glider

        speed_level = d_stat.speed + k_stat.speed + t_stat.speed + g_stat.speed
        accel_level = d_stat.acceleration + k_stat.acceleration + t_stat.acceleration + g_stat.acceleration
        weight_level = d_stat.weight + k_stat.weight + t_stat.weight + g_stat.weight
        handling_level = d_stat.handling + k_stat.handling + t_stat.handling + g_stat.handling
        traction_level = d_stat.traction + k_stat.traction + t_stat.traction + g_stat.traction
        miniturbo_level = d_stat.mini_Turbo + k_stat.mini_Turbo + t_stat.mini_Turbo + g_stat.miniTurbo
        invincibility_level = d_stat.invincibility + k_stat.invincibility + t_stat.invincibility + g_stat.invincibility

        return BuildStatsResponse(
            driver=driver.name,
            kart=kart.name,
            tire=tire.name,
            glider=glider.name,
            speed=StatDetail(level=speed_level, value=(speed_level + 3) / 4.0),
            acceleration=StatDetail(level=accel_level, value=(accel_level + 3) / 4.0),
            weight=StatDetail(level=weight_level, value=(weight_level + 3) / 4.0),
            handling=StatDetail(level=handling_level, value=(handling_level + 3) / 4.0),
            traction=StatDetail(level=traction_level, value=(traction_level + 3) / 4.0),
            mini_Turbo=StatDetail(level=mini_turbo_level, value=(mini_turbo_level + 3) / 4.0),
            invincibility=StatDetail(level=invincibility_level, value=(invincibility_level + 3) / 4.0)
        )
