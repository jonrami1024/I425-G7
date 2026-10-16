# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class tireBase(BaseModel):
    tire_id: int
    name: str
    tire_group_id: int
    image_file: str

    model_config = ConfigDict(
        from_attributes=True
    )

class TireRead(tireBase):
    pass