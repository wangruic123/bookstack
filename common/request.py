# common/request.py
import requests
from requests.adapters import HTTPAdapter
from common.log import logger
from common.config import ConfigLoader


class RequestContext:
    _shared_data = {}  # 类级别共享数据

    @classmethod
    def save_data(cls, key, value):
        cls._shared_data[key] = value

    @classmethod
    def get_data(cls, key, default=None):
        return cls._shared_data.get(key, default)


class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
        self.context = RequestContext()  # 注入上下文

    def send_request(self, method, url, data=None, headers=None):
        # 渲染动态参数（如 {{ temp_token }}）
        rendered_headers = self._render_template(headers)
        rendered_data = self._render_template(data)

        response = self.session.request(
            method=method,
            url=url,
            json=rendered_data,
            headers=rendered_headers
        )
        return response

    def _render_template(self, data):
        """使用 Jinja2 模板引擎渲染动态参数"""
        from jinja2 import Template
        if isinstance(data, dict):
            rendered = {}
            for k, v in data.items():
                if isinstance(v, str) and "{{" in v:
                    template = Template(v)
                    rendered[k] = template.render(self.context._shared_data)
                else:
                    rendered[k] = v
            return rendered
        return data

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