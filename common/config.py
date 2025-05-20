import configparser
from pathlib import Path


class ConfigLoader:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent
        self.config = configparser.ConfigParser()

    def load_ini(self, filename):
        cfg_path = self.base_path / 'conf' / filename
        self.config.read(cfg_path)
        return self.config