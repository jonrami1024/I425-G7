import os
import secrets
from dotenv import load_dotenv

# Read settings from the .env file (the .env file is not included in the zip or GitHub)
load_dotenv()

# Authentication configuration settings
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

if not SECRET_KEY:
    # No .env file: use a temporary key so the app still starts.
    # Tokens made with a temporary key stop working when the server restarts.
    print("WARNING: SECRET_KEY is not set. Copy .env.example to .env and set a secret key.")
    SECRET_KEY = secrets.token_urlsafe(64)
