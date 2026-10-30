# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlalchemy import func, or_, and_
from sqlalchemy.sql.functions import user
from sqlmodel import select, Session
from fastapi import HTTPException
from api.users.models import Users
from api.users.schemas import PaginationMeta, UserPage
from api.utilities.sorting import apply_sorting


class UserService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_users(self, limit: int | None = None, offset: int = 0, sort: str | None = None):
        return self.paginate_users(limit = limit, offset = offset, sort=sort)
    def fetch_user(self, user_id):
        user = self.session.get(Users, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def fetch_user_builds(self, user_id: int):
        user = self.fetch_user(user_id)
        if not user.builds:
            raise HTTPException(status_code=404, detail="No builds found for this user")
        return user.builds

    def fetch_user_build(self, user_id: int, build_id: int):
        user = self.fetch_user(user_id)
        build = next((b for b in user.builds if b.build_id == build_id), None)
        if not build:
            raise HTTPException(status_code=404, detail="Build not found for this user")
        return build

    def fetch_user_ratings(self, user_id: int):
        user = self.fetch_user(user_id)
        if not user.ratings:
            raise HTTPException(status_code=404, detail="No ratings found for this user")
        return user.ratings

    def paginate_users(
            self,
    limit: int | None = None,
    offset: int = 0, sort: str | None = None) -> UserPage:
        total_stmt = select(func.count()).select_from(Users)
        total = self.session.exec(total_stmt).one()
        if total == 0:
            raise HTTPException(status_code=404, detail="There isnt any users in the database")
        if limit is None:
            limit = total
        stmt = select(Users).offset(offset).limit(limit)

        if sort is not None:
            stmt = apply_sorting(stmt, sort, Users)

        users = self.session.exec(stmt).all()
        total_pages = (total + limit -1) // limit
        current_page = (offset // limit) + 1
        next_page = current_page + 1 if offset + limit < total else None
        previous_page = current_page - 1 if current_page > 1 else None
        return UserPage(
            meta=PaginationMeta(
                limit=limit,
                offset=offset,
                total=total,
                total_pages=total_pages,
                current_page=current_page,
                next_page=next_page,
                previous_page=previous_page,
                sort=sort),
            users = users
        )

    # slightly different from practice 10 since theres no numbers to convert
    def search_users(self,
                     q: str | None = None,
                     logic: str = "or"):
        stmt = select(Users)
        if q:
            words = [w.strip() for w in q.split(",") if w.strip()]
            conditions = []

            for word in words:
                pattern = f"%{word}%"
                conditions.append(or_(
                    Users.username.ilike(pattern),
                    Users.email.ilike(pattern)
                ))
            if conditions:
                stmt = stmt.where(and_(*conditions) if logic.lower() == "and" else or_(*conditions))
        users = self.session.exec(stmt).all()
        return users
