# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.builds.models import Builds

class BuildService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_builds(self):
        builds = self.session.exec(select(Builds)).all()
        if not builds:
            raise HTTPException(status_code=404, detail="No builds found")
        return builds
    def fetch_build(self, build_id):
        build = self.session.get(Builds, build_id)
        if not build:
            raise HTTPException(status_code=404, detail="No build found")
        return build
