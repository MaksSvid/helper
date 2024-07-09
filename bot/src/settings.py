import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings: 
    BOT_TOKEN: str = os.environ.get('BOT_TOKEN')
    BOT_NAME: str = os.environ.get('BOT_NAME')
    BOT_USERNAME: str = os.environ.get('BOT_USERNAME')
    DB_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    DB_USER: str = os.environ.get('POSTGRES_USER')
    DB_NAME: str = os.environ.get('POSTGRES_DB')
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: int = 5432

settings = Settings()