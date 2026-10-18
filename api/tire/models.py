# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
if TYPE_CHECKING:
    from api.tireGroup.models import tireGroup
    from api.builds.models import Builds

class Tires(SQLModel, table=True):
    __tablename__ = "tires"
    tire_id: int = Field(primary_key=True)
    name: str
    tire_group_id: int = Field(foreign_key="tire_groups.tire_group_id")
    image_file: str

    tire_group: "tireGroup" = Relationship(back_populates="tires")
    builds: list["Builds"] = Relationship(back_populates="tire")