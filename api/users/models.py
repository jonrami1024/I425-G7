# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: models.py
# Description:

from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from api.builds.models import Builds
    from api.build_ratings.models import Ratings

class Users(SQLModel, table=True):
    __tablename__ = "users"
    user_id: int = Field(primary_key=True)
    username: str
    email: str

    builds: list["Builds"] = Relationship(back_populates="user")
    ratings: list["Ratings"] = Relationship(back_populates="user")
