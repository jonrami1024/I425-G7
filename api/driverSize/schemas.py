# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class driverSizeBase(BaseModel):
    driver_group_id: int
    label: str
    size: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    traction: int
    mini_turbo: int
    invincibility: int

    model_config = ConfigDict(
        from_attributes = True
    )

class driverSizeRead(driverSizeBase):
    pass