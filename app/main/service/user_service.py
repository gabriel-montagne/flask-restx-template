import uuid
import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.user_roles import UserRole


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            roles=data['roles'],
            registered_on=datetime.datetime.utcnow(),
            oauth_id=data['oauth_id'],
            oauth_type=data['oauth_type']
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def update_user_roles(public_id, data):
    user = User.query.filter_by(public_id=public_id).first()
    if user:
        roles = [u.name for u in UserRole.query.all()]
        not_roles = [r for r in data['roles'] if r not in roles]
        if not_roles:
            response_object = {
                'status': 'fail',
                'message': 'Roles do not exist',
                'roles': not_roles
            }
            return response_object, 401

        user.roles = data['roles']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'User roles updated.',
            'roles': user.roles
        }
        return response_object, 200

    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist. Please register.',
        }
        return response_object, 401


def get_all_users():
    response_object = {
        'status': 'success',
        'users': [{'username': u.username, 'public_id': u.public_id}
                  for u in User.query.all()],
    }
    return response_object, 200


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'public_id': user.public_id,
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()
