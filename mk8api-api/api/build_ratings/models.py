# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: models.py
# Description:
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.builds.models import Builds
    from api.users.models import Users

class Ratings(SQLModel, table=True):
    __tablename__ = "build_ratings"
    rating_id: int = Field(primary_key=True)
    build_id: int = Field(foreign_key="builds.build_id")
    user_id: int = Field(foreign_key="users.user_id")
    score: int

    build: "Builds" = Relationship(back_populates="ratings")
    user: "Users" = Relationship(back_populates="ratings")
