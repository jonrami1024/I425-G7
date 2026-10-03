# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:
import pydantic
from sqlmodel import select, Session
from fastapi import HTTPException
from api.tireGroup.models import tireGroup

class TireGroupService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_tireGroups(self):
        tireGroups = self.session.exec(select(tireGroup)).all()
        if not tireGroups:
            raise HTTPException(status_code=404, detail="Tire Group not found")
        return tireGroups
    def fetch_tireGroup(self, tireGroup_name: str):
        tire_group = self.session.get(tireGroup, tireGroup_name)
        if not tire_group:
            raise HTTPException(status_code=404, detail="Tire Group not found")
        return tire_group
    def fetch_tireGroups_tires(self, tireGroup_name: str):
        tire_group = self.fetch_tireGroup(tireGroup_name)
        if not tire_group.tires:
            raise HTTPException(status_code=404, detail="Tires not found")
        return tire_group.tires