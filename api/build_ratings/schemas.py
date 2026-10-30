# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from typing import Optional

from pydantic import BaseModel, ConfigDict
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
class RatingPage(BaseModel):
    meta: PaginationMeta
    ratings: list[RatingRead]