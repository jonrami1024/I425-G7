# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from typing import Optional

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

class PaginationMeta(BaseModel):
    limit: int
    offset: int
    total: int
    total_pages: int
    current_page: int
    next_page: Optional[int] = None
    previous_page: Optional[int] = None

class UserPage(BaseModel):
    meta: PaginationMeta
    users: list[UserRead]