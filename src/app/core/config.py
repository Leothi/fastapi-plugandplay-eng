from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "FastAPI Plug and Play"
    version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"

    environment: str = "development"

    cors_origins: list[str] = Field(default_factory=lambda: ["*"])

    log_level: str = "INFO"
    log_json: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
