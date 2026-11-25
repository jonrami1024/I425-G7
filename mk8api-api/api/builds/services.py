# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlalchemy import func
from sqlmodel import select, Session, or_, and_
from fastapi import HTTPException
from api.builds.models import Builds
from api.build_ratings.models import Ratings
from api.builds.schemas import BuildPage, PaginationMeta
from api.calculateStats.services import CalculateStatsService
from api.calculateStats.schemas import BuildStatsRead, BuildParts
from api.utilities.sorting import apply_sorting


from api.builds.schemas import BuildCreate, BuildUpdate
from api.users.schemas import DeleteResponse
from api.users.models import Users
from api.driver.models import Drivers
from api.body.models import Bodies
from api.tire.models import Tires
from api.glider.models import Gliders

class BuildService:
    def __init__(self, session: Session):
        self.session = session

    def fetch_builds(self, limit: int | None = None, offset: int = 0, sort: str | None = None):
        return self.paginate_builds(limit=limit, offset=offset, sort=sort)

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

    def paginate_builds(self,
                         limit: int | None = None,
                         offset: int = 0, sort: str | None = None) -> BuildPage:
        total_stmt = select(func.count()).select_from(Builds)
        total = self.session.exec(total_stmt).one()
        if limit is None:
            limit = total or 1
        stmt = select(Builds).offset(offset).limit(limit)

        if sort is not None:
            stmt = apply_sorting(stmt, sort, Builds)

        builds = self.session.exec(stmt).all()
        total_pages = (total + limit - 1) // limit
        current_page = (offset // limit) + 1
        next_page = current_page + 1 if offset + limit < total else None
        previous_page = current_page - 1 if current_page > 1 else None
        return BuildPage(
            meta=PaginationMeta(
                limit=limit,
                offset=offset,
                total=total,
                total_pages=total_pages,
                current_page=current_page,
                next_page=next_page,
                previous_page=previous_page,
                sort=sort),
            builds=builds
        )
    # slightly different from practice 10 since most of the data are numbers
    def search_builds(self,
                      q: str | None = None,
                      logic: str = "or"):
        stmt = select(Builds)
        if q:
            words = [w.strip() for w in q.split(",") if w.strip()]
            conditions = []
            for word in words:
                try:
                    num = int(word)
                    conditions.append(or_(
                        Builds.driver_id == num,
                        Builds.body_id == num,
                        Builds.tire_id == num,
                        Builds.glider_id == num,
                        Builds.user_id == num,
                        Builds.build_id == num
                    ))
                except ValueError:
                    pattern = f"%{word}%"
                    conditions.append(or_(
                        Builds.build_name.ilike(pattern)
                    ))
            if conditions:
                stmt = stmt.where(and_(*conditions) if logic.lower() == "and" else or_(*conditions))

        builds = self.session.exec(stmt).all()
        return builds

    def fetch_build_user(self, build_id: int):
        return self.fetch_build(build_id).user

    def fetch_build_driver(self, build_id: int):
        return self.fetch_build(build_id).driver

    def fetch_build_body(self, build_id: int):
        return self.fetch_build(build_id).body

    def fetch_build_tire(self, build_id: int):
        return self.fetch_build(build_id).tire

    def fetch_build_glider(self, build_id: int):
        return self.fetch_build(build_id).glider

    # ---------- Lab 3: create, update, delete ----------
    def check_parts(self, data: dict):
        for field, model, name in [("user_id", Users, "User"), ("driver_id", Drivers, "Driver"), ("body_id", Bodies, "Body"),
                                   ("tire_id", Tires, "Tire"), ("glider_id", Gliders, "Glider")]:
            if data.get(field) is not None and not self.session.get(model, data[field]):
                raise HTTPException(status_code=404, detail=f"{name} {data[field]} not found")

    def create_build(self, build_data: BuildCreate) -> Builds:
        self.check_parts(build_data.model_dump())
        build = Builds(**build_data.model_dump())
        self.session.add(build)
        self.session.commit()
        self.session.refresh(build)
        return build

    def update_build(self, build_id: int, build_data: BuildUpdate) -> Builds:
        build = self.fetch_build(build_id)
        update_data = build_data.model_dump(exclude_unset=True)
        self.check_parts(update_data)
        for key, value in update_data.items():
            setattr(build, key, value)
        self.session.add(build)
        self.session.commit()
        self.session.refresh(build)
        return build

    def delete_build(self, build_id: int) -> DeleteResponse:
        build = self.fetch_build(build_id)
        for rating in self.session.exec(select(Ratings).where(Ratings.build_id == build_id)).all():
            self.session.delete(rating)
        self.session.delete(build)
        self.session.commit()
        return DeleteResponse(success=True, deleted_id=build_id)
