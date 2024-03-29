from flask import request
from flask_restx import Resource

from app.main.service.authentication_helper import login_user, logout_user
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return login_user(data=post_data)

    @api.route('/logout')
    class LogoutAPI(Resource):
        """
        Logout Resource
        """

        @api.doc('logout a user')
        def post(self):
            # get auth token
            auth_header = request.headers.get('Authorization')
            return logout_user(data=auth_header)
