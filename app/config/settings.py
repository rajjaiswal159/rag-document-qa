from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Google Gemini API Key
    GOOGLE_API_KEY: str

    # Maximum upload size (10 MB)
    MAX_FILE_SIZE: int = 10 * 1024 * 1024

    # Supported file types
    ALLOWED_EXTENSIONS: list[str] = ["pdf"]

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()