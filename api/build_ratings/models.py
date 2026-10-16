# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: models.py
# Description:
from sqlmodel import SQLModel, Field

class Ratings(SQLModel, table=True):
    __tablename__ = "build_ratings"
    rating_id: int = Field(primary_key=True)
    build_id: int = Field(foreign_key="builds.build_id")
    user_id: int = Field(foreign_key="users.user_id")
    score: int
