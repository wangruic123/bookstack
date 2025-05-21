# tools/data_generator.py
import random
import string
from datetime import datetime
from pathlib import Path
import pandas as pd

class TestDataGenerator:
    @staticmethod
    def generate_vin():
        """生成随机车辆VIN码"""
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=17))

    @staticmethod
    def generate_user_data(num=100):
        """生成用户测试数据集"""
        data = []
        for _ in range(num):
            user_id = f"U{random.randint(100000, 999999)}"
            username = f"user_{random.randint(1, 1000)}"
            phone = f"1{random.randint(30, 89)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}"
            data.append({
                "user_id": user_id,
                "username": username,
                "phone": phone,
                "reg_date": datetime.now().strftime("%Y-%m-%d")
            })
        return pd.DataFrame(data)

    @staticmethod
    def save_to_excel(df, filename="test_data.xlsx"):
        """保存数据到Excel"""
        output_path = Path(__file__).parent.parent / "caseparams" / filename
        df.to_excel(output_path, index=False)
        print(f"测试数据已生成：{output_path}")

if __name__ == "__main__":
    # 示例：生成100条用户数据
    df = TestDataGenerator.generate_user_data(100)
    TestDataGenerator.save_to_excel(df)