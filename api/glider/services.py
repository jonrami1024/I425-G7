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
    def fetch_glider(self, glider_id):
        glider = self.session.get(Gliders, glider_id)
        if not glider:
            raise HTTPException(status_code=404, detail="Glider not found")
        return glider
    def fetch_glider_builds(self, part_id: int):
        part = self.fetch_glider(part_id)
        if not part.builds:
            raise HTTPException(status_code=404, detail="No builds use this part")
        return part.builds
