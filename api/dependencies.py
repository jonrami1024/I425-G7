# Jonathan Ramirez-Molina
# Date: 10/1/2026
# File: dependencies.py
# Description:
from fastapi import Depends, HTTPException
from typing import Annotated, List

from jose import jwt, JWTError
from sqlmodel import Session
from starlette import status

from api.database import get_session
from fastapi.security import OAuth2PasswordBearer

from api.config import SECRET_KEY, ALGORITHM
from api.users.services import UserService
from api.users.models import Users

# database connection
SessionDep = Annotated[Session, Depends(get_session)]

# Authentication dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    session: SessionDep,
    token: str = Depends(oauth2_scheme)
) -> Users:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise credentials_exception

    try:
        user_id = int(payload.get("sub"))
    except (KeyError, TypeError, ValueError):
        raise credentials_exception

    user = UserService(session).fetch_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user

CurrentUserDep = Annotated[Users, Depends(get_current_user)]

# Generate a FastAPI dependency that checks the current user's role.
def role_required(required_roles: List[int]):
    def role_checker(current_user: CurrentUserDep):
        if current_user.role_id not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource."
            )
        return current_user

    return role_checker

# Create named RBAC dependencies for user roles.
AdminDep = Annotated[Users, Depends(role_required([1]))]
UserManagerDep = Annotated[Users, Depends(role_required([1, 2]))]
AdvancedUserDep = Annotated[Users, Depends(role_required([1, 3]))]
BasicUserDep = Annotated[Users, Depends(role_required([1, 2, 3, 4]))]