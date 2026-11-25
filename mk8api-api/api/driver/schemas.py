# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class DriverBase(BaseModel):
    driver_id: int
    name: str
    driver_group_id: int
    image_file: str

    model_config = ConfigDict(
        from_attributes = True
    )

class DriverRead(DriverBase):
    pass