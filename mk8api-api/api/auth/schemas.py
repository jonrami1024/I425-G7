from pydantic import Field, BaseModel
from api.users.schemas import UserAccount, UserBase

# Registration input: username, email, and password (role is always Basic User)
class UserRegister(UserAccount):
    pass

class UserLogin(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=8, max_length=20)

# Login output
class UserLoginResponse(BaseModel):
    jwt: str
    token_type: str
    user: UserBase
