# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.driverSize.models import driverSize

class Drivers(SQLModel, table=True):
    __tablename__ = "driver"
    driverName: str = Field(primary_key=True)
    driverSizeGroup: str = Field(foreign_key="driver_size.driverSizeGroup")
    driver_img: str

    driverSize: "driverSize" = Relationship(back_populates="drivers")

