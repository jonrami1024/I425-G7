from pydantic import Field, BaseModel
from api.users.schemas import UserCreate, UserBase

class UserRegister(UserCreate):
    # Set the password max length to 20 for plain password
    password: str = Field(min_length=8, max_length=20)

class UserLogin(BaseModel):
    username: str = Field(min_length=4, max_length=20)
    password: str = Field(min_length=8, max_length=20)

# Login output
class UserLoginResponse(BaseModel):
    jwt: str
    token_type: str
    user: UserBase