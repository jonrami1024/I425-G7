# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.tire.models import Tires

class tireGroup(SQLModel, table=True):
    __tablename__ = "tire_groups"
    tire_group_id: int = Field(primary_key=True)
    speed: int
    acceleration: int
    weight: int
    handling: int
    traction: int
    mini_turbo: int
    invincibility: int

    tires: list["Tires"] = Relationship(back_populates="tire_group")