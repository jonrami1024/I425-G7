# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from typing import Optional, TypedDict
from pydantic import BaseModel, ConfigDict


class KartBase(BaseModel):
    bodyName: str
    bodyTypeGroup: str
    body_img: str

    model_config = ConfigDict(
        from_attributes = True
    )

class KartRead(KartBase):
    pass
