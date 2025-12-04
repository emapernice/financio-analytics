import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / "config" / ".env"

load_dotenv(ENV_PATH)

class Settings:
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST")
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")

    @property
    def DATABASE_URL(self):
        return (
            f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}/{self.MYSQL_DATABASE}"
        )

settings = Settings()
