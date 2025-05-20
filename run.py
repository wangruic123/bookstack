import pytest
import os

if __name__ == '__main__':
    # 运行测试并生成Allure结果
    pytest.main()

    # 生成Allure报告（需要已安装Allure命令行工具）
    os.system("allure generate ./log/allure_results -o ./log/allure_report --clean")
    os.system("allure open ./log/allure_report")