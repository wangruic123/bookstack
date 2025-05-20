import requests
from common.log import logger


class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
        self.timeout = 10

    def send(self, method, url, **kwargs):
        try:
            res = self.session.request(
                method.upper(),
                url,
                timeout=self.timeout,
                **kwargs
            )
            logger.info(f"Request: {method} {url} | Status: {res.status_code}")
            return res
        except Exception as e:
            logger.error(f"Request failed: {str(e)}")
            raise