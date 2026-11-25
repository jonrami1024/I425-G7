# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from typing import Optional

from pydantic import BaseModel, ConfigDict

from typing import Self
from pydantic import Field, field_validator, model_validator

class BuildBase(BaseModel):
    build_id: int
    user_id: int
    driver_id: int
    body_id: int
    tire_id: int
    glider_id: int
    build_name: str

    model_config = ConfigDict(
        from_attributes = True
    )

class BuildRead(BuildBase):
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
class BuildPage(BaseModel):
    meta: PaginationMeta
    builds: list[BuildRead]

# ---------- Lab 3: input validation for create and update ----------

class BuildCreate(BaseModel):
    user_id: int = Field(..., ge=1)
    driver_id: int = Field(..., ge=1)
    body_id: int = Field(..., ge=1)
    tire_id: int = Field(..., ge=1)
    glider_id: int = Field(..., ge=1)
    build_name: str = Field(..., min_length=3, max_length=40)

    @field_validator("build_name", mode='after')
    @classmethod
    def build_name_cannot_be_blank(cls, value):
        value = value.strip()
        if len(value) < 3:
            raise ValueError('Build name must have at least 3 characters that are not spaces')
        return value

class BuildUpdate(BaseModel):
    driver_id: Optional[int] = Field(default=None, ge=1)
    body_id: Optional[int] = Field(default=None, ge=1)
    tire_id: Optional[int] = Field(default=None, ge=1)
    glider_id: Optional[int] = Field(default=None, ge=1)
    build_name: Optional[str] = Field(default=None, min_length=3, max_length=40)

    @field_validator("build_name", mode='after')
    @classmethod
    def build_name_cannot_be_blank(cls, value):
        if value is None:
            return value
        value = value.strip()
        if len(value) < 3:
            raise ValueError('Build name must have at least 3 characters that are not spaces')
        return value

    @model_validator(mode='after')
    def at_least_one_field(self) -> Self:
        if all(getattr(self, f) is None for f in ("driver_id", "body_id", "tire_id", "glider_id", "build_name")):
            raise ValueError('Provide at least one field to update')
        return self
