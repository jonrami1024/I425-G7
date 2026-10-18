# Jonathan Ramirez-Molina
# Date: 10/16/2026
# File: services.py
# Description:
from sqlmodel import select, Session
from fastapi import HTTPException
from api.build_ratings.models import Ratings

class RatingsService:
    def __init__(self, session: Session):
        self.session = session
    def fetch_ratings(self):
        ratings = self.session.exec(select(Ratings)).all()
        if not ratings:
            raise HTTPException(status_code=404, detail="No ratings found")
        return ratings
    def fetch_rating(self, rating_id):
        rating = self.session.get(Ratings, rating_id)
        if not rating:
            raise HTTPException(status_code=404, detail="Rating not found")
        return rating