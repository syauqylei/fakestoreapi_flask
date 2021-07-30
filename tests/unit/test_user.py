import sys, os
import pytest
from src.models.user import User


@pytest.fixture(scope='module')
def new_user():
    user = User({
        'name': 'admin',
        'email': 'admin@mail.com',
        'password': 'password'
    })
    yield user


def test_new_user(new_user):
    assert new_user.email == 'admin@mail.com'
    assert new_user.name == 'admin'
