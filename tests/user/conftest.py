import pytest

from config import BASE_URL
from src.user.helpers import UserHelper


@pytest.fixture(scope="session")
def user_helper():
	return UserHelper(BASE_URL)
