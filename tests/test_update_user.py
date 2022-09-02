from helpers.url import base_url, ApiBaseUrl


def test_update():
    response = base_url().put(ApiBaseUrl.users_url + '/1', data={"name": "George Michael", "job": "Software Engineer"})
    assert response.status_code == 200
    assert str(response.json()['name']) == 'George Michael'