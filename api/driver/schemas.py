# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: schemas.py
# Description:
from typing import Optional
from pydantic import BaseModel, ConfigDict

class DriverBase(BaseModel):
    driverName: str
    driverSizeGroup: str
    driver_img: str


model_config = ConfigDict(
    from_attributes = True
)

class DriverRead(DriverBase):
    pass