# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.driverSize.models import driverSize
    from api.builds.models import Builds

class Drivers(SQLModel, table=True):
    __tablename__ = "drivers"
    driver_id: int = Field(primary_key=True)
    name: str
    driver_group_id: int = Field(foreign_key="driver_groups.driver_group_id")
    image_file: str

    driverSize: "driverSize" = Relationship(back_populates="drivers")
    builds: list["Builds"] = Relationship(back_populates="driver")

