# tools/bulk_runner.py
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


class BulkRunner:
    @staticmethod
    def run_tests(environments=["DEV", "TEST"], parallel=False):
        """批量执行多环境测试"""
        base_cmd = ["python", "run.py", "--alluredir=./log/allure-results"]

        if parallel:
            base_cmd.insert(1, "-n")
            base_cmd.insert(2, "4")

        with ThreadPoolExecutor() as executor:
            for env in environments:
                cmd = base_cmd + [f"--env={env}"]
                executor.submit(subprocess.run, cmd)
                print(f"已启动{env}环境测试任务")


if __name__ == "__main__":
    # 示例：并行执行双环境测试
    BulkRunner.run_tests(environments=["DEV", "TEST"], parallel=True)