# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: schemas.py
# Description:
from pydantic import BaseModel, ConfigDict

class GliderBase(BaseModel):
    glider: str
    gliderGroup: str
    glider_img: str

    model_config = ConfigDict(
        from_attributes=True
    )

class GliderRead(GliderBase):
    pass