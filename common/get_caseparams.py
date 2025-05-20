import yaml
import pandas as pd
from pathlib import Path


class DataLoader:
    @staticmethod
    def load_yaml(file_name):
        path = Path(__file__).parent.parent / 'caseparams' / file_name
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    @staticmethod
    def load_excel(file_name, sheet_name=0):
        path = Path(__file__).parent.parent / 'caseparams' / file_name
        return pd.read_excel(path, sheet_name=sheet_name).to_dict('records')