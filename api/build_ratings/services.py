# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlalchemy import func
from sqlmodel import select, Session
from fastapi import HTTPException
from api.build_ratings.models import Ratings
from api.build_ratings.schemas import RatingPage, PaginationMeta
from api.utilities.sorting import apply_sorting


from api.build_ratings.schemas import RatingCreate, RatingUpdate
from api.users.schemas import DeleteResponse
from api.users.models import Users
from api.builds.models import Builds

class RatingsService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_ratings(self, limit: int | None = None, offset: int = 0, sort: str | None = None) -> RatingPage:
        return self.paginate_ratings(limit = limit, offset = offset, sort = sort)
    def fetch_rating(self, rating_id):
        rating = self.session.get(Ratings, rating_id)
        if not rating:
            raise HTTPException(status_code=404, detail="Rating not found")
        return rating
    def fetch_rating_build(self, rating_id: int):
        return self.fetch_rating(rating_id).build

    def fetch_rating_user(self, rating_id: int):
        return self.fetch_rating(rating_id).user

    def paginate_ratings(self,
                         limit: int | None = None,
                         offset: int = 0, sort: str | None = None) -> RatingPage:
        total_stmt = select(func.count()).select_from(Ratings)
        total = self.session.exec(total_stmt).one()
        if limit is None:
            limit = total or 1
        stmt = select(Ratings).offset(offset).limit(limit)

        if sort is not None:
            stmt = apply_sorting(stmt, sort, Ratings)

        ratings = self.session.exec(stmt).all()
        total_pages = (total + limit - 1) // limit
        current_page = (offset // limit) + 1
        next_page = current_page + 1 if offset + limit < total else None
        previous_page = current_page - 1 if current_page > 1 else None
        return RatingPage(
            meta=PaginationMeta(
                limit=limit,
                offset=offset,
                total=total,
                total_pages=total_pages,
                current_page=current_page,
                next_page=next_page,
                previous_page=previous_page,
                sort=sort),
            ratings=ratings
        )

    # ---------- Lab 3: create, update, delete ----------
    def create_rating(self, rating_data: RatingCreate) -> Ratings:
        build = self.session.get(Builds, rating_data.build_id)
        if not build:
            raise HTTPException(status_code=404, detail=f"Build {rating_data.build_id} not found")
        if not self.session.get(Users, rating_data.user_id):
            raise HTTPException(status_code=404, detail=f"User {rating_data.user_id} not found")
        if build.user_id == rating_data.user_id:
            raise HTTPException(status_code=409, detail="Users cannot rate their own build")
        already = self.session.exec(select(Ratings).where(Ratings.build_id == rating_data.build_id,
                                                          Ratings.user_id == rating_data.user_id)).first()
        if already:
            raise HTTPException(status_code=409, detail="This user has already rated this build")
        rating = Ratings(**rating_data.model_dump())
        self.session.add(rating)
        self.session.commit()
        self.session.refresh(rating)
        return rating

    def update_rating(self, rating_id: int, rating_data: RatingUpdate) -> Ratings:
        rating = self.fetch_rating(rating_id)
        update_data = rating_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(rating, key, value)
        self.session.add(rating)
        self.session.commit()
        self.session.refresh(rating)
        return rating

    def delete_rating(self, rating_id: int) -> DeleteResponse:
        rating = self.fetch_rating(rating_id)
        self.session.delete(rating)
        self.session.commit()
        return DeleteResponse(success=True, deleted_id=rating_id)
