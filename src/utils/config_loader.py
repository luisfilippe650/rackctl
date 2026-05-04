import os
import yaml

CONFIG_DIR = os.path.expanduser("~/.config/rackctl")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yaml")

DEFAULT_CONFIG = {
    "api_url": "http://localhost:8000/v1",
    "timeout": 10
}


def ensure_config():
    """
    Garante que o arquivo de config existe.
    Se não existir, cria com valores padrão.
    """
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            yaml.dump(DEFAULT_CONFIG, f)


def load_config():
    ensure_config()

    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)