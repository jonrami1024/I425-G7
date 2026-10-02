# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: services.py
# Description:

from sqlmodel import select, Session
from fastapi import HTTPException
from api.driver.models import Drivers

class DriverService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_drivers(self):
        drivers = self.session.exec(select(Drivers)).all()
        if not drivers:
            raise HTTPException(status_code=404, detail="No drivers found")
        return drivers
    def fetch_driver(self, driverName):
        driver = self.session.get(Drivers, driverName)
        if not driver:
            raise HTTPException(status_code=404, detail="No driver found")
        return driver
    def fetch_driver_driverSize(self, driverName: str):
        driver = self.fetch_driver(driverName)
        if not driver.driverSize:
            raise HTTPException(status_code=404, detail="Driver size not found for driver")
        return driver.driverSize