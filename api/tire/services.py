# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:

from sqlmodel import select, Session
from fastapi import HTTPException
from api.tire.models import Tires

class TireService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_tires(self):
        tires = self.session.exec(select(Tires)).all()
        if not tires:
            raise HTTPException(status_code=404, detail="Tires not found")
        return tires
    def fetch_tire(self, tire_id):
        tire = self.session.get(Tires, tire_id)
        if not tire:
            raise HTTPException(status_code=404, detail="Tire not found")
        return tire
    def fetch_tire_tireGroup(self, tire_id: int):
        tire_obj = self.fetch_tire(tire_id)
        if not tire_obj.tire_group:
            raise HTTPException(status_code=404, detail="Tire Group not found")
        return tire_obj.tire_group
    def fetch_tire_builds(self, part_id: int):
        part = self.fetch_tire(part_id)
        if not part.builds:
            raise HTTPException(status_code=404, detail="No builds use this part")
        return part.builds
