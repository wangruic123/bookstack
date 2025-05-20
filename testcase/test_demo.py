import allure
import pytest


@allure.feature("认证模块")
class TestLogin:
    @allure.story("用户登录")
    @pytest.mark.smoke
    def test_login(self, api_client, test_data):
        case_data = test_data[0]

        with allure.step("1. 发送登录请求"):
            response = api_client.send_request(
                method=case_data["method"],
                url=case_data["url"],
                headers=case_data["headers"],
                json=case_data["data"]
            )

        with allure.step("2. 验证响应结果"):
            assert response.status_code == 200
            assert "token" in response.text

