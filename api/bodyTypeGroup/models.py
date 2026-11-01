# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.body.models import Bodies

class BodyGroups(SQLModel, table=True):
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

    bodies: list["Bodies"] = Relationship(back_populates="body_group")