# common/config.py
import configparser
from pathlib import Path


class ConfigLoader:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.base_path = Path(__file__).parent.parent
            cls._instance.config = configparser.ConfigParser()
        return cls._instance

    def get_interface_config(self, env='DEV'):
        cfg_path = self.base_path / 'conf' / 'interface.ini'
        self.config.read(cfg_path)
        return dict(self.config[env])

    def get_db_config(self):
        cfg_path = self.base_path / 'conf' / 'base.ini'
        self.config.read(cfg_path)
        return dict(self.config['DATABASE'])