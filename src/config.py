import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("RACK_API_URL", "http://localhost:8000/v1")