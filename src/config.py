from src.utils.config_loader import load_config

config = load_config()

BASE_URL = config.get("api_url")
TIMEOUT = config.get("timeout", 10)