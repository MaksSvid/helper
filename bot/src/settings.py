import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings: 
    BOT_TOKEN: str = os.environ.get('BOT_TOKEN')
    BOT_NAME: str = os.environ.get('BOT_NAME')
    BOT_USERNAME: str = os.environ.get('BOT_USERNAME')

settings = Settings()