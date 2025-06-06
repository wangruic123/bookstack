# testcase/test_login.py
import pytest
import allure
from common.get_caseparams import DataLoader
from common.request import RequestHandler
from common.extract_utils import Extractor
from testcase.conftest import token_storage


@allure.feature("登录模块")
class TestLogin:
    @pytest.mark.parametrize("case", DataLoader.load_case("login.yaml"))
    def test_get_temp_token(self, case, token_storage):
        """获取并存储临时Token"""
        req = RequestHandler()

        # 发送请求
        response = req.request(
            method=case["method"],
            endpoint=case["url"],
            json=case.get("data"),
            headers=case.get("headers")
        )

        # 验证状态码
        assert response.status_code == case["expected"]["status_code"]

        # 提取并存储Token
        extract_config = case["expected"].get("extract", {})
        for key, config in extract_config.items():
            value = Extractor.extract_value(response, config)
            if value:
                # 存储到全局Token存储
                setattr(token_storage, key, value)
                allure.attach(
                    name=f"Extracted {key}",
                    body=value,
                    attachment_type=allure.attachment_type.TEXT
                )
            else:
                pytest.fail(f"未能提取到 {key}")