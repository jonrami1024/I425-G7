# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    user_id: int
    username: str
    email: str

    model_config = ConfigDict(
        from_attributes = True
    )

class UserRead(UserBase):
    pass