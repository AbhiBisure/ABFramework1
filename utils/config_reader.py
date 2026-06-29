import json
from pathlib import Path

class ConfigReader:

    def __init__(self, env):
        self.env = env
        config_path = Path(__file__).parent.parent / "data" / "config.json"
        with open(config_path,"r") as f:
            self.data = json.load(f)[self.env]

    def get(self, key):
        return self.data.get(key)

#If you ask for a key that does not exist (like asking for "username" under the "UAT" environment from your previous example),
# .get() will quietly return None instead of throwing a disruptive KeyError.
