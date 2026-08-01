import pytest

from api_client import (
    get_users,
    get_user,
    create_user,
    update_user_put,
    update_user_patch,
    delete_user
)


@pytest.fixture
def users_response():
    return get_users()


@pytest.fixture
def single_user_response():
    return get_user(1)


@pytest.fixture
def created_user():
    return create_user()


@pytest.fixture
def updated_user_put():
    return update_user_put(1)


@pytest.fixture
def updated_user_patch():
    return update_user_patch(1)


@pytest.fixture
def deleted_user():
    return delete_user(1)