from buggy_api import *


def test_status_code():
    response = get_users()
    assert response.status_code == 200


def test_json():
    data = get_user()
    assert data["id"] == 1


def test_create_user():
    response = create_user()
    assert response.status_code == 201