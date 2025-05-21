# common/request.py
import requests
from requests.adapters import HTTPAdapter
from common.log import logger
from common.config import ConfigLoader


class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries=3))
        self.config = ConfigLoader().get_interface_config()
        self.base_url = self.config['base_url']
        self.timeout = int(self.config['timeout'])

    def request(self, method, endpoint, **kwargs):
        full_url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(
                method=method.upper(),
                url=full_url,
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()
            logger.info(f"请求成功：{method} {full_url}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"请求失败：{str(e)}")
            raise