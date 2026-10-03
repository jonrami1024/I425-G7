# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.bodyTypeGroup.models import kartType

class Karts(SQLModel, table=True):
    __tablename__ = "body"
    bodyName: str = Field(primary_key=True)
    bodyTypeGroup: str = Field(foreign_key="bodyTypeGroup.bodyTypeGroup")
    body_img: str

    kartType: "kartType" = Relationship(back_populates="karts")


