from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "CreatorOS Multi-Agent Intelligence Hub"
    ENV: str = "dev"

    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    POSTGRES_URL: str
    REDIS_URL: str

    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str

    JWT_SECRET: str

    class Config:
        env_file = ".env"


settings = Settings()