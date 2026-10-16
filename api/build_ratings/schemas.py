# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
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