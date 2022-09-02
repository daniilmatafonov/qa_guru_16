from helpers.url import base_url, ApiBaseUrl


def test_not_found_user():
    response = base_url().get(ApiBaseUrl.not_found_url + '/23')
    assert response.status_code == 404