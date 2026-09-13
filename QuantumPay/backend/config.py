from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "QuantumPay API"
    DATABASE_URL: str = "sqlite:///./quantumpay.db"
    RP_ID: str = "localhost"
    RP_NAME: str = "QuantumPay"
    ORIGIN: str = "http://localhost:8000"
    CHALLENGE_TTL_SECONDS: int = 300

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
