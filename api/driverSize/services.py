# Jonathan Ramirez-Molina
# Date: 10/2/2026
# File: services.py
# Description:


from sqlmodel import select, Session
from fastapi import HTTPException
from api.driverSize.models import DriverGroups




class DriverGroupService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_driverSizes(self):
        driverSizes = self.session.exec(select(DriverGroups)).all()
        return driverSizes
    def fetch_driverSize(self, driver_group_id: int):
        driver_size = self.session.get(DriverGroups, driver_group_id)
        if not driver_size:
            raise HTTPException(status_code=404, detail="Driver group not found")
        return driver_size
    def fetch_driverSize_drivers(self, driver_group_id: int):
        driver_size = self.fetch_driverSize(driver_group_id)
        return driver_size.drivers
