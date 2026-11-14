import secrets

# Authentication configuration settings
SECRET_KEY = secrets.token_urlsafe(64)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30