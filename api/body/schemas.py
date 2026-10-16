# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from typing import Optional, TypedDict
from pydantic import BaseModel, ConfigDict


class KartBase(BaseModel):
    body_id: int
    name: str
    vehicle_type: str
    body_group_id: int
    image_file: str

    model_config = ConfigDict(
        from_attributes = True
    )

class KartRead(KartBase):
    pass
