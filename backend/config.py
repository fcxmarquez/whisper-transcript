import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
    ENV = os.environ.get("FLASK_ENV", "production")
    CORS_ORIGIN = os.environ.get("CORS_ORIGIN", "http://localhost:5173")
    WHISPER_MODEL = os.environ.get("WHISPER_MODEL", "base")


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"


class ProductionConfig(Config):
    DEBUG = False
    ENV = "production"
