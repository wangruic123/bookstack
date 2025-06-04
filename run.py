# run.py
import pytest
import os
import shutil

def clear_history():
    """清理历史数据"""
    results_dir = "./../report/allure-results"
    report_dir = "./../report/report/allure-report"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)

if __name__ == "__main__":
    clear_history()
    pytest.main(["-s", "-v", "--alluredir=./../report/allure-results"])
    os.system("allure generate ./../report/allure-results -o ./../report/allure-report --clean")
    os.system("allure open ./../report/allure-report")