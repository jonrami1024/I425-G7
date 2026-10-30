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
    def paginate_ratings(self,
                         limit: int | None = None,
                         offset: int = 0, sort: str | None = None) -> RatingPage:
        total_stmt = select(func.count()).select_from(Ratings)
        total = self.session.exec(total_stmt).one()
        if total == 0:
            raise HTTPException(status_code=404,
                                detail="There isn't any ratings in the database")
        if limit is None:
            limit = total
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