"""Configuration management using pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from platformdirs import user_cache_dir


class Settings(BaseSettings):
    """Application settings for Lixinger API proxy."""

    # Required: Lixinger API token
    lxr_api_token: str

    # Cache settings
    cache_ttl_seconds: int = 36000  # 10 hours
    cache_max_size: int = 5000  # Maximum number of cached items

    # Rate limiting settings
    rate_limit_window_seconds: int = 60  # 1 minute
    rate_limit_max_requests: int = 10  # Max 10 requests per window
    rate_limit_max_wait_seconds: int = 600  # Max wait time: 10 minutes

    # Cache directory using platformdirs
    @property
    def cache_dir(self) -> str:
        """Get the cache directory path."""
        return user_cache_dir("lxrtools", "wisdomvalley")

    # Upstream API base URL
    upstream_api_base: str = "https://open.lixinger.com/api"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


# Global settings instance
settings = Settings()
