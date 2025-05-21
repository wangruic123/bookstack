# common/testcasetemplate.py
import allure
import pytest
from common.request import RequestHandler
from common.assertion import Assertion

class BaseTestCase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = RequestHandler()
        self.asserter = Assertion()