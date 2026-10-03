# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:

from typing import Optional
from pydantic import BaseModel, ConfigDict

class kartTypeBase(BaseModel):
    bodyTypeGroup: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    miniTurbo: int
    invincibility: int

    model_config = ConfigDict(
        from_attributes= True
    )

class kartTypeRead(kartTypeBase):
    pass