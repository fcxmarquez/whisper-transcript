import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'audio_inputs'
    MODEL_SIZE = os.environ.get('MODEL_SIZE') or 'medium'
