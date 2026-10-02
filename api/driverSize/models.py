# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.driver.models import Drivers

class driverSize(SQLModel, table=True):
    __tablename__ = "driver_size"
    driverSizeGroup: str = Field(primary_key=True)
    speed: int
    acceleration: int
    weight: int
    handling: int
    miniTurbo: int
    invincibility: int

    drivers: list["Drivers"] = Relationship(back_populates="driverSize")