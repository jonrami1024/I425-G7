# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.body.models import Karts

class kartType(SQLModel, table=True):
    __tablename__ = "body_groups"
    body_group_id: int = Field(primary_key=True)
    label: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    traction: int
    mini_turbo: int
    invincibility: int

    karts: list["Karts"] = Relationship(back_populates="kartType")