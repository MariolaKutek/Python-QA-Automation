def test_get_users_status(users_response):
    assert users_response.status_code == 200


def test_get_single_user(single_user_response):
    assert single_user_response.status_code == 200
    assert single_user_response.json()["id"] == 1


def test_create_user(created_user):
    assert created_user.status_code == 201


def test_update_put(updated_user_put):
    assert updated_user_put.status_code == 200


def test_update_patch(updated_user_patch):
    assert updated_user_patch.status_code == 200


def test_delete(deleted_user):
    assert deleted_user.status_code == 200