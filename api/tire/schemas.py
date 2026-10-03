# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class tireBase(BaseModel):
    tire: str
    tireGroup: str
    tire_img: str

    model_config = ConfigDict(
        from_attributes=True
    )

class TireRead(tireBase):
    pass