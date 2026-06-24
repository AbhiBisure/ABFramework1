import json
from pathlib import Path

class ConfigReader:

    def __init__(self, env):
        config_path = Path(__file__).parent.parent / "data" / "config.json"

        with open(config_path, "r") as f:
            data = json.load(f)

        self.config = data[env.upper()]

    def get(self, key):
        return self.config.get(key)