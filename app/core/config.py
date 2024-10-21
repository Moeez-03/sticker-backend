from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_BUCKET_NAME: str
    DO_SPACES_KEY: str
    DO_SPACES_SECRET: str
    DO_BUCKET_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
