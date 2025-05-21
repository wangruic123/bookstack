# common/get_caseparams.py
import yaml
import pandas as pd
from pathlib import Path


class DataLoader:
    @classmethod
    def load_yaml(cls, filename):
        path = Path(__file__).parent.parent / 'caseparams' / filename
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    @classmethod
    def load_excel(cls, filename, sheet_name=0):
        path = Path(__file__).parent.parent / 'caseparams' / filename
        df = pd.read_excel(path, sheet_name=sheet_name)
        return df.to_dict('records')

    @classmethod
    def load_case(cls, file_name):
        if file_name.endswith('.yaml'):
            return cls.load_yaml(file_name)
        elif file_name.endswith('.xlsx'):
            return cls.load_excel(file_name)
        raise ValueError("不支持的文件格式")