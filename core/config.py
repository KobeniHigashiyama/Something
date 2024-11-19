from pydantic_settings import BaseSettings
from pathlib import Path

Base_Dir = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{Base_Dir}/db.sqlite3"
    db_echo: bool = True


settings = Settings()
