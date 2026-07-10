from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Google Gemini API key
    GOOGLE_API_KEY: str

    # Maximum allowed upload size (10 MB)
    MAX_FILE_SIZE: int = 10 * 1024 * 1024

    # Expiration time of vector databases
    DOCUMENT_EXPIRATION_MINUTES: int = 10

    # Allowed file extensions
    ALLOWED_EXTENSIONS: list[str] = ["pdf"]

    # Directory for storing Data
    VECTOR_STORE_PATH: str = "data/vector_store"
    SAVED_pdf_PATH: str = "data/uploads"
    DATABASE_PATH: str = "data/documents.db"

    # Load configuration from the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


# Application settings instance
settings = Settings()