import os
import sys
import yaml
from dotenv import load_dotenv

"""
Configuration Management Module.

Priority order:
 1. If a config file exists at CONFIG_PATH, it must be a YAML mapping containing 'api_url'. If invalid, exit.
 2. Otherwise, use environment variables.
 3. Otherwise, use fallback defaults.
"""

load_dotenv()
CONFIG_PATH = os.getenv("RACKCTL_CONFIG", "/etc/rackctl/rackctl.yaml")

FALLBACK_CONFIG = {
    "api_url": "http://localhost:8000/v1/racktables",
    "timeout": 10
}


def load_config_from_file(path):
    try:
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            return data
    except Exception as e:
        print(f"[-] Error reading configuration file ({path}): {e}")
        return None

_file_config = load_config_from_file(CONFIG_PATH)

if os.path.exists(CONFIG_PATH):
    # config file is present; it must be a mapping with 'api_url'
    if not isinstance(_file_config, dict):
        print(f"[-] Invalid configuration file format at {CONFIG_PATH}: expected YAML mapping.")
        sys.exit(1)
    if 'api_url' not in _file_config or not _file_config.get('api_url'):
        print(f"[-] 'api_url' missing or empty in configuration file ({CONFIG_PATH}).")
        sys.exit(1)
    api_url = _file_config.get('api_url')
    if not isinstance(api_url, str) or not api_url.startswith(('http://', 'https://')):
        print(f"[-] Invalid api_url in configuration file ({CONFIG_PATH}): {api_url}")
        sys.exit(1)
    CONFIG = _file_config
else:
    # No file: use environment or fallback
    CONFIG = {
        'api_url': os.getenv('RACKCTL_API_URL', FALLBACK_CONFIG['api_url']),
        'timeout': int(os.getenv('RACKCTL_TIMEOUT', FALLBACK_CONFIG['timeout']))
    }

BASE_URL = CONFIG.get('api_url', FALLBACK_CONFIG['api_url'])
TIMEOUT = int(CONFIG.get('timeout', FALLBACK_CONFIG['timeout']))
