# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.glider.models import Gliders

class gliderGroup(SQLModel, table=True):
    __tablename__ = "gliderGroup"
    gliderGroup: str = Field(primary_key=True)
    speed: int
    acceleration: int
    weight: int
    handling: int
    miniTurbo: int
    invincibility: int

    gliders: list["Gliders"] = Relationship(back_populates="glider_group")