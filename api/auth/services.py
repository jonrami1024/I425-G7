from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
from api.users.services import UserService
from api.users.models import Users
from api.users.schemas import UserCreate, UserBase
from .schemas import UserRegister, UserLogin
from api.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta,timezone
from jose import jwt
from fastapi import HTTPException, status

class AuthService:
    password_hash = PasswordHash(hashers=[BcryptHasher()])

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    @staticmethod
    def hash_password(plain_password: str) -> str:
        return AuthService.password_hash.hash(plain_password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return AuthService.password_hash.verify(plain_password, hashed_password)

    @staticmethod
    def create_jwt_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def register_user(self, data: UserRegister) -> User:
        hashed_pw = AuthService.hash_password(data.password)

        user = UserCreate(
            email=data.email,
            username=data.username,
            password=hashed_pw
        )

        return self.user_service.create_user(user)

    def login_user(self, data: UserLogin):
        user = self.user_service.fetch_user_by_username(data.username)

        if not user or not AuthService.verify_password(data.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid credentials")

        # user's credentials are valid; create a token
        token_data = {"sub": str(user.user_id), "role_id": str(user.role_id)}
        token = AuthService.create_jwt_token(data=token_data)

        return {
            "jwt": token,
            "token_type": "bearer",
            "user": UserBase.model_validate(user, from_attributes=True)

        }
