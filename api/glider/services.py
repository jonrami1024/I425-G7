# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.glider.models import Gliders

class GliderService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_gliders(self):
        gliders = self.session.exec(select(Gliders)).all()
        if not gliders:
            raise HTTPException(status_code=404, detail="No gliders found")
        return gliders
    def fetch_glider(self, glider):
        glider = self.session.get(Gliders, glider)
        if not glider:
            raise HTTPException(status_code=404, detail="No glider found")
        return glider
    def fetch_glider_gliderGroup(self, glider: str):
        glider_obj = self.fetch_glider(glider)
        if not glider_obj.glider_group:
            raise HTTPException(status_code=404, detail="Glider Group not found")
        return glider_obj.glider_group