import pytest
import allure
from common.request import RequestHandler
from common.get_caseparams import DataLoader


@allure.feature("车主工具接口")
class TestGetOwnerTools:
    @allure.story("获取车主工具列表")
    @pytest.mark.parametrize("case", DataLoader.load_yaml("getownertools.yaml"))
    def test_get_owner_tools(self, case):
        req = RequestHandler()

        with allure.step("1. 发送接口请求"):
            response = req.send(
                method=case["method"],
                url=case["url"],
                headers=case["headers"],
                params=case["params"]
            )

        with allure.step("2. 验证响应结果"):
            assert response.status_code == 200
            assert case["expected"] in response.text