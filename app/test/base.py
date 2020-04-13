from flask_testing import TestCase
import datetime
import uuid

from app.main import db
from manage import app
from app.main.model.user import User
from app.main.controller.user_role_controller import create_update_role


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()
        create_roles(['user', 'admin'])

    def tearDown(self):
        db.session.remove()
        db.drop_all()


def create_test_users(n):
    users = []
    for i in range(n):
        user = User(
            public_id=str(uuid.uuid4()),
            email=f'email_{i + 1}@user.com',
            username=f'username_{i + 1}',
            password=f'password_{i + 1}',
            registered_on=datetime.datetime.utcnow(),
            oauth_id=f'oauth_id_{i + 1}',
            oauth_type=f'GOOGLE'
        )
        db.session.add(user)
        users.append(user)
    db.session.commit()
    return users


def create_roles(roles):
    for role in roles:
        create_update_role({'name': role})
