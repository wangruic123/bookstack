# testcase/test_getownertools.py
import pytest
import allure
from common.request import RequestHandler
from common.get_caseparams import DataLoader
from common.assertion import Assertion


@allure.feature("车主工具接口测试")
class TestOwnerTools:
    @allure.story("获取车主工具列表")
    @pytest.mark.parametrize("case", DataLoader.load_yaml("getownertools.yaml"))
    def test_get_tools(self, case):
        req = RequestHandler()
        test_data = case["test_data"]

        with allure.step("1. 发送接口请求"):
            response = req.request(
                method=test_data["method"],
                endpoint=test_data["url"],
                headers=test_data.get("headers"),
                params=test_data.get("params")
            )

        with allure.step("2. 验证响应结果"):
            Assertion.assert_status_code(response, 200)
            Assertion.assert_key_exists(response.json(), "toolList")