# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
if TYPE_CHECKING:
    from api.tireGroup.models import tireGroup

class Tires(SQLModel, table=True):
    __tablename__ = "tire"
    tire: str = Field(primary_key=True)
    tireGroup: str = Field(foreign_key="tireGroup.tireGroup")
    tire_img: str

    tire_group: "tireGroup" = Relationship(back_populates="tires")