from helpers.url import base_url
import logging

logging.basicConfig(level=logging.DEBUG)


def test_users_list():
    response = base_url().get('/api/users?page=2')
    assert response.status_code == 200