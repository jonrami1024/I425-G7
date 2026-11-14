# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlalchemy import func, or_, and_
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select, Session
from fastapi import HTTPException, status
from api.users.models import Users
from api.users.schemas import PaginationMeta, UserPage
from api.utilities.sorting import apply_sorting
from datetime import datetime, timezone



from api.users.schemas import UserCreate, UserUpdate, DeleteResponse
from api.builds.models import Builds
from api.build_ratings.models import Ratings

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
    def create_user(self, user_data: UserCreate) -> Users:
        try:
            user = Users(**user_data.dict())
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user

        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error: Unable to create user record",
            ) from e

    def update_user(self, user_id: int, user_data: UserUpdate) -> Users:
        def update_user(self, user_id: int, user_data: UserUpdate):
            user = self.fetch_user(user_id)
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            try:
                update_data = user_data = user_data.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(user, key, value)

                user.updated_at = datetime.now(timezone.utc)

                self.session.add(user)
                self.session.commit()
                self.session.refresh(user)
                return user

            except SQLAlchemyError as e:
                self.session.rollback()
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Database error: Unable to update user record",
                ) from e

    def delete_user(self, user_id: int) -> None:
        # Retrieve the user by id
        user = self.fetch_user(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

        try:
            self.session.delete(user)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error: Unable to delete the user record",
            ) from e

    def fetch_user_builds(self, user_id: int):
        user = self.fetch_user(user_id)
        return user.builds

    def fetch_user_build(self, user_id: int, build_id: int):
        user = self.fetch_user(user_id)
        build = next((b for b in user.builds if b.build_id == build_id), None)
        if not build:
            raise HTTPException(status_code=404, detail="Build not found for this user")
        return build

    def fetch_user_ratings(self, user_id: int):
        user = self.fetch_user(user_id)
        return user.ratings

    def paginate_users(
            self,
    limit: int | None = None,
    offset: int = 0, sort: str | None = None) -> UserPage:
        total_stmt = select(func.count()).select_from(Users)
        total = self.session.exec(total_stmt).one()
        if limit is None:
            limit = total or 1
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

    # ---------- Lab 3: create, update, delete ----------
    def check_unique(self, username: str | None, email: str | None, user_id: int | None = None):
        if username is not None:
            taken = self.session.exec(select(Users).where(Users.username == username)).first()
            if taken and taken.user_id != user_id:
                raise HTTPException(status_code=409, detail="Username is already taken")
        if email is not None:
            taken = self.session.exec(select(Users).where(Users.email == email)).first()
            if taken and taken.user_id != user_id:
                raise HTTPException(status_code=409, detail="Email is already taken")

    def create_user(self, user_data: UserCreate) -> Users:
        self.check_unique(user_data.username, user_data.email)
        user = Users(**user_data.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update_user(self, user_id: int, user_data: UserUpdate) -> Users:
        user = self.fetch_user(user_id)
        update_data = user_data.model_dump(exclude_unset=True)
        self.check_unique(update_data.get("username"), update_data.get("email"), user_id)
        for key, value in update_data.items():
            setattr(user, key, value)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete_user(self, user_id: int) -> DeleteResponse:
        user = self.fetch_user(user_id)
        # remove the user's ratings, the ratings on the user's builds, and the user's builds
        for rating in self.session.exec(select(Ratings).where(Ratings.user_id == user_id)).all():
            self.session.delete(rating)
        for build in self.session.exec(select(Builds).where(Builds.user_id == user_id)).all():
            for rating in self.session.exec(select(Ratings).where(Ratings.build_id == build.build_id)).all():
                self.session.delete(rating)
            self.session.delete(build)
        self.session.delete(user)
        self.session.commit()
        return DeleteResponse(success=True, deleted_id=user_id)

    def fetch_user_by_username(self, username):
        stmt = select(Users).where(Users.username == username)

        return self.session.exec(stmt).first()
