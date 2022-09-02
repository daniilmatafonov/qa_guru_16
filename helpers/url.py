import os
from requests import Session


class ApiBaseUrl(Session):
    users_url = "/api/users"
    not_found_url = "/api/unknown"

    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        return super().request(method, url=f'{self.base_url}{url}', **kwargs)


def base_url() -> ApiBaseUrl:
    api_base_url = os.getenv('URL', "https://reqres.in")
    return ApiBaseUrl(base_url=api_base_url)
