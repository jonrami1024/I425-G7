# Jonathan Ramirez-Molina
# Date: 10/3/2026
# File: services.py
# Description:

from sqlmodel import select, Session
from fastapi import HTTPException
from .models import kartType

class KartTypeService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_kartTypes(self):
        kartTypes = self.session.exec(select(kartType)).all()
        if not kartTypes:
            raise HTTPException(status_code=404, detail="No body groups found")
        return kartTypes
    def fetch_kartType(self, body_group_id: str):
        kart_Type = self.session.get(kartType, body_group_id)
        if not kart_Type:
            raise HTTPException(status_code=404, detail="Body group not found")
        return kart_Type
    def fetch_kartType_karts(self, body_group_id: str):
        kart_Type = self.fetch_kartType(body_group_id)
        if not kart_Type.karts:
            raise HTTPException(status_code=404, detail="No bodies found for this body group")
        return kart_Type.karts