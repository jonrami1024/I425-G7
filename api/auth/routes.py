from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from api.auth.schemas import UserRegister, UserLogin, UserLoginResponse
from api.auth.services import AuthService
from api.dependencies import SessionDep
from api.users.schemas import UserRead
from api.users.services import UserService

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Reuse existing user service dependency
def get_user_service(session: SessionDep) -> UserService:
    return UserService(session)

# Define AuthService dependency
def get_auth_service(user_service: UserService = Depends(get_user_service)) -> AuthService:
    return AuthService(user_service)

# Annotated dependency
AuthServiceDep = Annotated[AuthService, Depends(get_auth_service)]

@router.post("/register", response_model=UserRead, status_code=201)
def register(service: AuthServiceDep, user: UserRegister):
    return service.register_user(user)

@router.post("/login", status_code=201, response_model=UserLoginResponse)
def login_user(service: AuthServiceDep, data: UserLogin):
    return service.login_user(data)