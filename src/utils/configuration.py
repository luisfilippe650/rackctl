import os
import yaml
from dotenv import load_dotenv

"""
Configuration Management Module.

This module loads the rackctl settings from:
    1. Environment variables (via .env)
    2. /etc/rackctl/rackctl.yaml

The file is automatically created during package installation.
If the file is missing or invalid, fallback values are used.
"""

# Carrega variáveis de ambiente do arquivo .env, se existir
load_dotenv()

CONFIG_PATH = os.getenv("RACKCTL_CONFIG", "/etc/rackctl/rackctl.yaml")

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
            return data if data else FALLBACK_CONFIG

    except yaml.YAMLError as e:
        print(f"[-] Error parsing configuration file ({CONFIG_PATH}): {e}")
        return FALLBACK_CONFIG
    except Exception:
        return FALLBACK_CONFIG


config = load_config()

# Prioridade: Variável de ambiente > Arquivo de Configuração > Fallback
BASE_URL = os.getenv("RACKCTL_API_URL", config.get("api_url", FALLBACK_CONFIG["api_url"]))
TIMEOUT = int(os.getenv("RACKCTL_TIMEOUT", config.get("timeout", FALLBACK_CONFIG["timeout"])))