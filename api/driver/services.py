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
    def fetch_driver(self, driver_id):
        driver = self.session.get(Drivers, driver_id)
        if not driver:
            raise HTTPException(status_code=404, detail="Driver not found")
        return driver
    def fetch_driver_driverSize(self, driver_id: str):
        driver = self.fetch_driver(driver_id)
        if not driver.driverSize:
            raise HTTPException(status_code=404, detail="Driver group not found for this driver")
        return driver.driverSize
    def fetch_driver_builds(self, part_id: int):
        part = self.fetch_driver(part_id)
        if not part.builds:
            raise HTTPException(status_code=404, detail="No builds use this part")
        return part.builds
