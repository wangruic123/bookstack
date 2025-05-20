import pytest
import configparser
import yaml
from common.request import RequestUtil

@pytest.fixture(scope="session")
def env_config():
    """读取环境配置"""
    config = configparser.ConfigParser()
    config.read('conf/base.ini', encoding='utf-8')
    return config['DEV']  # 切换环境时修改这里

@pytest.fixture(scope="function")
def test_data(request):
    """参数化读取YAML测试数据"""
    case_name = request.node.name
    with open(f'caseparams/{case_name}.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture(scope="session")
def api_client(env_config):
    """创建全局请求会话"""
    return RequestUtil(base_url=env_config['base_url'])