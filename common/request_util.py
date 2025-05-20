import requests
from requests.adapters import HTTPAdapter

class RequestUtil:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.session.mount('http://', HTTPAdapter(max_retries=3))
        self.base_url = base_url

    def send_request(self, method, url, **kwargs):
        full_url = f"{self.base_url}{url}"
        response = self.session.request(method.upper(), full_url, **kwargs)
        response.raise_for_status()
        return response