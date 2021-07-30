import pytest
import os
from src.app import create_app
from src.models import db

env_name = os.getenv('FLASK_ENV')


@pytest.fixture(scope='session')
def test_client():
    flask_app = create_app(env_name)

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            db.session.commit()
            yield testing_client
            db.session.remove()
            db.drop_all()
