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
            raise HTTPException(status_code=404, detail="Kart type not found")
        return kartTypes
    def fetch_kartType(self, bodyTypeGroup: str):
        kart_Type = self.session.get(kartType, bodyTypeGroup)
        if not kart_Type:
            raise HTTPException(status_code=404, detail="Kart type not found")
        return kart_Type
    def fetch_kartType_karts(self, bodyTypeGroup: str):
        kart_Type = self.fetch_kartType(bodyTypeGroup)
        if not kart_Type.karts:
            raise HTTPException(status_code=404, detail="Kart type not found")
        return kart_Type.karts