import os
import yaml

"""
Configuration Management Module.
This module loads the 'rackctl' settings from /etc/default/rackctl.
The file is installed by the package and can be customized by the user.
If the file is missing or invalid, fallback values are used.
"""

CONFIG_PATH = "/etc/default/rackctl"

FALLBACK_CONFIG = {
    "api_url": "http://localhost:8000/v1",
    "timeout": 10
}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return FALLBACK_CONFIG

    try:
        with open(CONFIG_PATH, "r") as f:
            data = yaml.safe_load(f)
            return data if data else FALLBACK_CONFIG
    except Exception:
        return FALLBACK_CONFIG


config = load_config()

BASE_URL = config.get("api_url", FALLBACK_CONFIG["api_url"])
TIMEOUT = config.get("timeout", FALLBACK_CONFIG["timeout"])