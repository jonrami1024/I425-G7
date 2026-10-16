# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.gliderGroup.models import gliderGroup

class Gliders(SQLModel, table=True):
    __tablename__ = "gliders"
    glider_id: int = Field(primary_key=True)
    name: str
    image_file: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    traction: int
    mini_turbo: int
    invincibility: int