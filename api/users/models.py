# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: models.py
# Description:

from sqlmodel import SQLModel, Field

class Users(SQLModel, table=True):
    __tablename__ = "users"
    user_id: int = Field(primary_key=True)
    username: str
    email: str