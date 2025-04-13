from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str

    # Application settings
    DEBUG: bool = False
    PROJECT_NAME: str = "Restaurant Booking API"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()
