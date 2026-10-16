# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.gliderGroup.models import gliderGroup

class GliderGroupService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_gliderGroups(self):
        gliderGroups = self.session.exec(select(gliderGroup)).all()
        if not gliderGroups:
            raise HTTPException(status_code=404, detail="Glider Group not found")
        return gliderGroups
    def fetch_gliderGroup(self, glider_group_id: str):
        glider_group = self.session.get(gliderGroup, glider_group_id)
        if not glider_group:
            raise HTTPException(status_code=404, detail="Glider Group not found")
        return glider_group
    def fetch_gliderGroup_gliders(self, glider_group_id: str):
        glider_group = self.fetch_gliderGroup(glider_group_id)
        if not glider_group.gliders:
            raise HTTPException(status_code=404, detail="Gliders not found")
        return glider_group.gliders