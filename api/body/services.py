# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.body.models import Karts

class KartService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_karts(self):
        karts = self.session.exec(select(Karts)).all()
        if not karts:
            raise HTTPException(status_code=404, detail="No Karts found")
        return karts
    def fetch_kart(self, body_id):
        kart = self.session.get(Karts, body_id)
        if not kart:
            raise HTTPException(status_code=404, detail="No Kart found")
        return kart
    def fetch_kart_kartType(self, body_id: int):
        kart = self.fetch_kart(body_id)
        if not kart.kartType:
            raise HTTPException(status_code=404, detail="No Kart Type found")
        return kart.kartType
