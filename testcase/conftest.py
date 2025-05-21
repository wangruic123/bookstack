# testcase/conftest.py
import pytest
import allure
import configparser
from pathlib import Path
from common.config import ConfigLoader
from common.get_caseparams import DataLoader
from common.log import logger
from common.request import RequestHandler


@pytest.fixture(scope="session", autouse=True)
def global_setup():
    """全局初始化操作"""
    logger.info("================ 测试启动 ================")
    yield
    logger.info("================ 测试结束 ================")


@pytest.fixture(scope="session")
def env_config(request):
    """读取环境配置（支持命令行指定环境）"""
    # 从命令行获取环境参数，默认DEV环境
    env = request.config.getoption("--env", default="DEV")
    config = ConfigLoader().get_interface_config(env)

    # 在Allure报告中记录环境信息
    allure.environment(
        BASE_URL=config["base_url"],
        ENV=env,
        TIMEOUT=config["timeout"]
    )
    return config


@pytest.fixture(scope="function")
def test_data(request):
    """动态加载参数化数据"""
    case_file = request.node.get_closest_marker("data_source").args[0]
    return DataLoader.load_case(case_file)


@pytest.fixture(scope="class")
def api_client(env_config):
    """创建API请求客户端"""
    return RequestHandler()


@pytest.fixture(scope="session")
def db_connection():
    """数据库连接（按需使用）"""
    from common.selectDB import DBClient
    client = DBClient()
    yield client
    client.conn.close()


def pytest_addoption(parser):
    """添加自定义命令行参数"""
    parser.addoption(
        "--env",
        action="store",
        default="DEV",
        choices=["DEV", "TEST"],
        help="选择测试环境：DEV/TEST"
    )
    parser.addoption(
        "--parallel",
        action="store_true",
        default=False,
        help="启用并行测试"
    )


def pytest_configure(config):
    """配置Allure报告元数据"""
    config._metadata["项目名称"] = "二手车接口测试平台"
    config._metadata["测试范围"] = "核心业务接口"
    config._metadata["维护团队"] = "质量保障部"