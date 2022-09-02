from helpers.url import base_url, ApiBaseUrl


def test_users_list():
    response = base_url().get(ApiBaseUrl.users_url, params="page=2")
    assert response.status_code == 200