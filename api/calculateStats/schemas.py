from pydantic import BaseModel

class StatDetail(BaseModel):
    level: int
    value: float

class StatsBlock(BaseModel):
    speed: StatDetail
    acceleration: StatDetail
    weight: StatDetail
    handling: StatDetail
    traction: StatDetail
    mini_turbo: StatDetail
    invincibility: StatDetail

class CombinationRead(BaseModel):
    driver: str
    body: str
    tire: str
    glider: str
    stats: StatsBlock

class BuildParts(BaseModel):
    driver: str
    body: str
    tire: str
    glider: str

class BuildStatsRead(BaseModel):
    build_id: int
    build_name: str
    parts: BuildParts
    stats: StatsBlock
