# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class gliderGroupBase(BaseModel):
    glider_group_id: int
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

class gliderGroupRead(gliderGroupBase):
    pass