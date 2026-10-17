# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.users.models import Users

class UserService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_users(self):
        users = self.session.exec(select(Users)).all()
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return users
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
