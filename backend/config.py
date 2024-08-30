import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    WHISPER_MODEL = os.environ.get("WHISPER_MODEL") or "medium"
