from pydantic import BaseModel

class StatDetail(BaseModel):
    level: int
    value: float

class BuildStatsResponse(BaseModel):
    driver: str
    kart: str
    tire: str
    glider: str
    speed: StatDetail
    acceleration: StatDetail
    weight: StatDetail
    handling: StatDetail
    traction: StatDetail
    mini_Turbo: StatDetail
    invincibility: StatDetail
