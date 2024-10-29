import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file if not production
if os.environ.get("ENV") != "production":
	load_dotenv()

class Config(BaseSettings):
    API_KEY: str = os.getenv("API_KEY")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

config = Config()
