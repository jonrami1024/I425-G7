# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.body.models import Karts

class kartType(SQLModel, table=True):
    __tablename__ = "bodyTypeGroup"
    bodyTypeGroup: str = Field(primary_key=True)
    speed: int
    acceleration: int
    weight: int
    handling: int
    miniTurbo: int
    invincibility: int

    karts: list["Karts"] = Relationship(back_populates="kartType")