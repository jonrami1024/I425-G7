# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: database.py
# Description:

from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///api/database.sqlite"
conn_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True, connect_args=conn_args)

def get_session():
    with Session(engine) as session:
        yield session