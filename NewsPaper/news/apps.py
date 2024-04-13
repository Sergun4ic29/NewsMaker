from django.apps import AppConfig
import os
from dotenv import load_dotenv
from pathlib import Path


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'



dotenv_path = Path('C:\keysP')
load_dotenv(dotenv_path=dotenv_path)

EMAIL_PASS = os.getenv('EMAIL_PASS')
#SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
#STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')