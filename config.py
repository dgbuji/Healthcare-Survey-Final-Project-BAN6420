import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MONGO_URI = os.getenv('MONGO_URI')
    EXPORT_FOLDER = os.path.join(os.path.dirname(__file__), 'exports')
    os.makedirs(EXPORT_FOLDER, exist_ok=True)