# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from typing import Optional

from pydantic import BaseModel, ConfigDict
from pydantic import Field, StrictInt

class RatingBase(BaseModel):
    rating_id: int
    build_id: int
    user_id: int
    score: int

    model_config = ConfigDict(
        from_attributes=True
    )

class RatingRead(RatingBase):
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
class RatingPage(BaseModel):
    meta: PaginationMeta
    ratings: list[RatingRead]

# ---------- Lab 3: input validation for create and update ----------

class RatingCreate(BaseModel):
    build_id: int = Field(..., ge=1)
    user_id: int = Field(..., ge=1)
    score: StrictInt = Field(..., ge=1, le=5)

class RatingUpdate(BaseModel):
    score: Optional[StrictInt] = Field(default=None, ge=1, le=5)
