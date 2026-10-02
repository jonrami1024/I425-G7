# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: services.py
# Description:


from sqlmodel import select, Session
from fastapi import HTTPException
from api.driverSize.models import driverSize




class DriverSizeService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_driverSizes(self):
        driverSizes = self.session.exec(select(driverSize)).all()
        if not driverSizes:
            raise HTTPException(status_code=404, detail="No driver sizes found")
        return driverSizes
    def fetch_driverSize(self, driverSizeGroup: str):
        driver_size = self.session.get(driverSize, driverSizeGroup)
        if not driver_size:
            raise HTTPException(status_code=404, detail="No driver size group found")
        return driver_size
    def fetch_driverSize_drivers(self, driverSizeGroup: str):
        driver_size = self.fetch_driverSize(driverSizeGroup)
        if not driver_size.drivers:
            raise HTTPException(status_code=404, detail="No drivers found for this size group")
        return driver_size.drivers
