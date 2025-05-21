# common/assertion.py
from common.log import logger

class Assertion:
    @staticmethod
    def assert_status_code(response, expected_code):
        actual = response.status_code
        assert actual == expected_code, \
            f"Status code验证失败，预期:{expected_code}，实际:{actual}"
        logger.info(f"Status code验证成功：{expected_code}")

    @staticmethod
    def assert_key_exists(response_json, key):
        assert key in response_json, \
            f"响应中缺少关键字段：{key}"
        logger.info(f"字段存在性验证成功：{key}")