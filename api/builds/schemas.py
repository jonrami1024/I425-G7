# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: schemas.py
# Description:
from pydantic import BaseModel, ConfigDict

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