# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: dependencies.py
# Description:
from fastapi import Depends
from typing import Annotated
from sqlmodel import Session
from api.database import get_session

# database connection
SessionDep = Annotated[Session, Depends(get_session)]
