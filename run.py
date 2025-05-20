import pytest
import os

if __name__ == '__main__':
    # 清理历史结果
    os.system("rm -rf ./log/allure-results")

    # 执行测试用例
    pytest.main(["-s", "-v"])

    # 生成Allure报告
    os.system("allure generate ./log/allure-results -o ./log/allure-report --clean")
    os.system("allure open ./log/allure-report")