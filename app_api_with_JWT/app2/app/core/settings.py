# from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    # # Postgres
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DB: str
    # POSTGRES_PORT: str
    # POSTGRES_HOST: str
    # DEBUG: Optional[bool] = False
    #
    # # Email

    # Jwt
    # ACCESS_TOKEN_EXPIRES_IN_DAYS: int
    # REFRESH_TOKEN_EXPIRES_IN_DAYS: int
    # JWT_ALGORITHM: str
    # JWT_SECRET_KEY: str
    # ACCESS_TOKEN_EXPIRES_IN_DAYS = 15
    # REFRESH_TOKEN_EXPIRES_IN_DAYS = 30
    # JWT_SECRET_KEY = "your_secret_key_here"
    # JWT_ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRES_IN_DAYS = 2
    REFRESH_TOKEN_EXPIRES_IN_DAYS = 2
    JWT_ALGORITHM = "HS256"
    JWT_SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY4MTY1NTk4OCwiaWF0IjoxNjgxNjU1OTg4fQ.ADE6 - a6XcA3R5hVZiiY1mCUkj82HjADzCXBrUaRurFk"

    # # Pusher
    # PUSHER_APP_ID: Optional[str] = None
    # PUSHER_KEY: Optional[str] = None
    # PUSHER_SECRET: Optional[str] = None
    # PUSHER_CLUSTER: Optional[str] = None
    # PUSHER_SSL: Optional[bool] = True

    # # Channels
    # GENERAL_CHANNEL: Optional[str] = "general-channel"
    # ALL_CHANNEL: Optional[str] = "all-channel"
    #
    # # Cloud
    # CLOUD_NAME: str
    # API_KEY: str
    # API_SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
