# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: models.py
# Description:

from sqlmodel import SQLModel, Field, Relationship

class Builds(SQLModel, table=True):
    __tablename__ = "builds"
    build_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="users.user_id")
    driver_id: int = Field(foreign_key="driver.driver_id")
    body_id: int = Field(foreign_key="bodies.body_id")
    tire_id: int = Field(foreign_key="tires.tire_id")
    glider_id: int = Field(foreign_key="gliders.glider_id")
    build_name: str

    user: "Users" = Relationship(back_populates="builds")
    ratings: list["Ratings"] = Relationship(back_populates="build")
