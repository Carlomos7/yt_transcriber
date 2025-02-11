from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Dict, List, Union


class Settings(BaseSettings):
    """Application Configuration"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # General App Config
    app_name: str = Field(default="YouTube Transcriber", env="APP_NAME")
    debug: bool = Field(default=True, env="DEBUG")
    api_key: str = Field(..., env="API_KEY")

    # YouTube Downloader Options
    yt_username: str = Field(default="", env="YT_USERNAME")
    yt_password: str = Field(default="", env="YT_PASSWORD")
    yt_format: str = Field(default="bestaudio/best", env="YT_FORMAT")
    yt_nocheckcertificate: bool = Field(default=True, env="YT_NOCHECKCERTIFICATE")
    
    # Whisper Model Config
    whisper_model: str = Field(default="small", env="WHISPER_MODEL")

    # Output Config
    output_dir: str = Field(default="output", env="OUTPUT_DIR")

    @property
    def yt_dlp_options(self) -> Dict:
        """Returns yt-dlp options in a clean, reusable format"""
        return {
            "username": self.yt_username or None,  # Avoid empty string issues
            "password": self.yt_password or None,
            "format": self.yt_format,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "nocheckcertificate": self.yt_nocheckcertificate,
        }


# Singleton instance for easy import
settings = Settings()
