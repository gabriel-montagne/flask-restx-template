from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'oauth_id': fields.String(description='Oauth Identifier'),
        'oauth_type': fields.String(description='Oauth type (GOOGLE, FACEBOOK)')
    })


class UserRoleDto:
    api = Namespace('user_role', description='user roles related operations')
    user_role = api.model('user_role', {
        'name': fields.String(required=True, description='role name'),
        'description': fields.String(description='role description')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
