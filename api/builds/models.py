# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.users.models import Users
    from api.build_ratings.models import Ratings
    from api.driver.models import Drivers
    from api.body.models import Karts
    from api.tire.models import Tires
    from api.glider.models import Gliders

class Builds(SQLModel, table=True):
    __tablename__ = "builds"
    build_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    driver_id: int = Field(foreign_key="drivers.driver_id")
    body_id: int = Field(foreign_key="bodies.body_id")
    tire_id: int = Field(foreign_key="tires.tire_id")
    glider_id: int = Field(foreign_key="gliders.glider_id")
    build_name: str

    user: "Users" = Relationship(back_populates="builds")
    ratings: list["Ratings"] = Relationship(back_populates="build")
    driver: "Drivers" = Relationship(back_populates="builds")
    body: "Karts" = Relationship(back_populates="builds")
    tire: "Tires" = Relationship(back_populates="builds")
    glider: "Gliders" = Relationship(back_populates="builds")
