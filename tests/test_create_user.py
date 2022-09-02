import pytest
from dotenv import load_dotenv
from helpers.url import base_url, ApiBaseUrl


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def test_create():
    response = base_url().post(ApiBaseUrl.users_url, data={"name": "Neo", "job": "Saviour"})
    assert response.status_code == 201
