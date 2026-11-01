# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from typing import Optional

from pydantic import BaseModel, ConfigDict

from typing import Self
from pydantic import EmailStr, Field, constr, field_validator, model_validator

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
    sort: Optional[str] = None

class UserPage(BaseModel):
    meta: PaginationMeta
    users: list[UserRead]

# ---------- Lab 3: input validation for create and update ----------

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20, pattern=r'^[A-Za-z0-9_]+$')
    email: EmailStr = Field(..., max_length=100)

    @field_validator("username", mode='after')
    @classmethod
    def username_cannot_be_only_numbers(cls, value):
        if value.isdigit():
            raise ValueError('Username must contain at least one letter')
        return value

    @field_validator("email", mode='after')
    @classmethod
    def email_to_lowercase(cls, value):
        return value.lower()

class UserUpdate(BaseModel):
    username: Optional[constr(min_length=3, max_length=20, pattern=r'^[A-Za-z0-9_]+$')] = None
    email: Optional[EmailStr] = Field(default=None, max_length=100)

    @field_validator("username", mode='after')
    @classmethod
    def username_cannot_be_only_numbers(cls, value):
        if value is not None and value.isdigit():
            raise ValueError('Username must contain at least one letter')
        return value

    @field_validator("email", mode='after')
    @classmethod
    def email_to_lowercase(cls, value):
        return value.lower() if value is not None else value

    @model_validator(mode='after')
    def at_least_one_field(self) -> Self:
        if self.username is None and self.email is None:
            raise ValueError('Provide at least one field to update: username or email')
        return self

class DeleteResponse(BaseModel):
    success: bool
    deleted_id: int
