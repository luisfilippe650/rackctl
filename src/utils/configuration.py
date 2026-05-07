import os
import yaml

"""
Configuration Management Module.

This module loads the rackctl settings from:
    /etc/rackctl/rackctl.yaml

The file is automatically created during package installation.
If the file is missing or invalid, fallback values are used.

"""

CONFIG_PATH = "/etc/rackctl/rackctl.yaml"

FALLBACK_CONFIG = {
    "api_url": "http://localhost:8000/v1",
    "timeout": 10
}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return FALLBACK_CONFIG

    try:
        with open(CONFIG_PATH, "r") as file:
            data = yaml.safe_load(file)

            if not data:
                return FALLBACK_CONFIG

            return data

    except Exception:
        return FALLBACK_CONFIG


config = load_config()

BASE_URL = config.get("api_url", FALLBACK_CONFIG["api_url"])
TIMEOUT = config.get("timeout", FALLBACK_CONFIG["timeout"])