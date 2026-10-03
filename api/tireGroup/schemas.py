# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from pydantic import BaseModel, ConfigDict

class tireGroupBase(BaseModel):
    tireGroup: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    miniTurbo: int
    invincibility: int

    model_config = ConfigDict(
        from_attributes = True
    )

class tireGroupRead(tireGroupBase):
    pass