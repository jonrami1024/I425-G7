# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from pydantic import BaseModel, ConfigDict

class GliderBase(BaseModel):
    glider_id: int
    name: str
    image_file: str
    speed: int
    acceleration: int
    weight: int
    handling: int
    traction: int
    mini_turbo: int
    invincibility: int

    model_config = ConfigDict(
        from_attributes=True
    )

class GliderRead(GliderBase):
    pass