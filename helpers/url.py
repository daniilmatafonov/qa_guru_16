import os
from requests import Session

api_base_url = os.getenv('URL', "https://reqres.in/")


class ApiBaseUrl(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        return super().request(method, url=f'{self.base_url}{url}', **kwargs)


def base_url() -> ApiBaseUrl:
    return ApiBaseUrl(base_url=api_base_url)
