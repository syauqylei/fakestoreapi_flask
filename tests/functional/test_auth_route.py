import pytest
import json
from src.models.user import User


@pytest.fixture(scope='module')
def create_user():
    user = User({
        'name': 'rindu',
        'email': 'rindu@mail.com',
        'password': 'password'
    })
    user.save()
    yield user
    user.delete()


def test_login_success(test_client, create_user):
    response = test_client.post('/api/login',
                                data=json.dumps(
                                    dict(email='rindu@mail.com',
                                         password='password')),
                                content_type='application/json')

    data = json.loads(response.data)

    assert response.status == '200 OK'
    assert 'access_token' in data
    assert 'status' in data
    assert data['status'] == 'success'


def test_register_success(test_client, create_user):
    response = test_client.post('/api/register',
                                data=json.dumps(
                                    dict(email='sono@mail.com',
                                         password='password',
                                         name='sono')),
                                content_type='application/json')

    create_user.query.filter_by(name='rindu')
    data = json.loads(response.data)

    assert create_user.name == 'rindu'
    assert response.status == '201 CREATED'
    assert 'status' in data
    assert data['status'] == 'success'
