# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.gliderGroup.models import gliderGroup

class Gliders(SQLModel, table=True):
    __tablename__ = "glider"
    glider: str = Field(primary_key=True)
    gliderGroup: str = Field(foreign_key="gliderGroup.gliderGroup")
    glider_img: str

    glider_group: "gliderGroup" = Relationship(back_populates="gliders")