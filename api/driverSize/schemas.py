# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class driverSizeBase(BaseModel):
    driverSizeGroup: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    miniTurbo: int
    invincibility: int

    model_config = ConfigDict(
        from_attributes = True
    )

class driverSizeRead(driverSizeBase):
    pass