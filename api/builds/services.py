# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.builds.models import Builds
from api.build_ratings.models import Ratings
from api.calculateStats.services import CalculateStatsService
from api.calculateStats.schemas import BuildStatsRead, BuildParts

class BuildService:
    def __init__(self, session: Session):
        self.session = session

    def fetch_builds(self):
        builds = self.session.exec(select(Builds)).all()
        if not builds:
            raise HTTPException(status_code=404, detail="No builds found")
        return builds

    def fetch_build(self, build_id: int):
        build = self.session.get(Builds, build_id)
        if not build:
            raise HTTPException(status_code=404, detail="Build not found")
        return build

    def fetch_build_stats(self, build_id: int):
        build = self.fetch_build(build_id)
        stats_service = CalculateStatsService(self.session)
        combo = stats_service.calculate_build_stats(
            driver_id=build.driver_id,
            body_id=build.body_id,
            tire_id=build.tire_id,
            glider_id=build.glider_id
        )
        return BuildStatsRead(
            build_id=build.build_id,
            build_name=build.build_name,
            parts=BuildParts(driver=combo.driver, body=combo.body, tire=combo.tire, glider=combo.glider),
            stats=combo.stats
        )

    def fetch_build_ratings(self, build_id: int):
        self.fetch_build(build_id)
        ratings = self.session.exec(
            select(Ratings).where(Ratings.build_id == build_id)
        ).all()
        if not ratings:
            raise HTTPException(status_code=404, detail="No ratings found for this build")
        return ratings

    def fetch_build_rating(self, build_id: int, rating_id: int):
        self.fetch_build(build_id)
        rating = self.session.get(Ratings, rating_id)
        if not rating or rating.build_id != build_id:
            raise HTTPException(
                status_code=404, 
                detail=f"Rating {rating_id} not found for build {build_id}"
            )
        return rating
