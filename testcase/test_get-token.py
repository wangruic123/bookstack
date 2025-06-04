# testcase/test_login.py
import re

import pytest
import allure
from common.request import RequestHandler
from common.get_caseparams import DataLoader
from common.assertion import Assertion


@allure.feature("bookstack接口测试")
class TestLogin:
    @allure.story("登录")
    @pytest.mark.parametrize("case", DataLoader.load_yaml("get-token.yaml"))
    def test_token(self, case):
        req = RequestHandler()
        test_data = case["test_data"]

        with allure.step("1. 发送接口请求"):
            response = req.request(
                method=test_data["method"],
                endpoint=test_data["url"],
                headers=test_data.get("headers"),
                params=test_data.get("params")
            )
            html_response = response.text
            token_pattern = r'<meta\s+.*?name\s*=\s*["\']token["\'].*?content\s*=\s*["\'](.*?)["\'].*?>'
            token = re.search(token_pattern, html_response, re.IGNORECASE)
        with allure.step("2. 验证响应结果"):
            Assertion.assert_status_code(response, 200)
            Assertion.assert_key_exists(response.json(), "toolList")