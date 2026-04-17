from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool
    HOST: str
    PORT: int
    DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()