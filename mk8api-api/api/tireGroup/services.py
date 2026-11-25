# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:
import pydantic
from sqlmodel import select, Session
from fastapi import HTTPException
from api.tireGroup.models import TireGroups

class TireGroupService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_tireGroups(self):
        tireGroups = self.session.exec(select(TireGroups)).all()
        return tireGroups
    def fetch_tireGroup(self, tire_group_id: int):
        tire_group = self.session.get(TireGroups, tire_group_id)
        if not tire_group:
            raise HTTPException(status_code=404, detail="Tire Group not found")
        return tire_group
    def fetch_tireGroups_tires(self, tire_group_id: int):
        tire_group = self.fetch_tireGroup(tire_group_id)
        return tire_group.tires