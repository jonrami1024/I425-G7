# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.bodyTypeGroup.models import kartType
    from api.builds.models import Builds

class Karts(SQLModel, table=True):
    __tablename__ = "bodies"
    body_id: int = Field(primary_key=True)
    name: str
    vehicle_type: str
    body_group_id: int = Field(foreign_key="body_groups.body_group_id")
    image_file: str

    kartType: "kartType" = Relationship(back_populates="karts")
    builds: list["Builds"] = Relationship(back_populates="body")


