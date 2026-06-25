from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_URL: str
    ENVIRONMENT: str
    ACCESS_TOKEN_SECRET_KEY: str
    REFRESH_TOKEN_SECRET_KEY: str
    ALGORITHM: str
    REFRESH_TOKEN_EXPIRE: int
    ACCESS_TOKEN_EXPIRE: int
    ODOO_URL: str
    ODOO_PORT: int
    DB_NAME: str
    API_KEY: str
    REDIS_URL: str
    USER_NAME: EmailStr

    class Config:
        env_file = ".env"


settings = Settings()
