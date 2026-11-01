# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.body.models import Bodies

class BodyService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_karts(self):
        karts = self.session.exec(select(Bodies)).all()
        return karts
    def fetch_kart(self, body_id):
        kart = self.session.get(Bodies, body_id)
        if not kart:
            raise HTTPException(status_code=404, detail="Body not found")
        return kart
    def fetch_kart_kartType(self, body_id: int):
        kart = self.fetch_kart(body_id)
        if not kart.body_group:
            raise HTTPException(status_code=404, detail="Body group not found for this body")
        return kart.body_group
    def fetch_kart_builds(self, part_id: int):
        part = self.fetch_kart(part_id)
        return part.builds
