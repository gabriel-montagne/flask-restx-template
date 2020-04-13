from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.dto import UserRoleDto
from ..service.user_role_service import create_update_role, delete_role, get_all_roles

api = UserRoleDto.api
_user_role = UserRoleDto.user_role


@api.route('')
class UserRoleList(Resource):
    @api.doc('list_of_roles')
    @token_required
    @api.marshal_list_with(_user_role, envelope='data')
    def get(self):
        """List all roles"""
        return get_all_roles()

    @api.expect(_user_role, validate=True)
    @api.response(201, 'Role successfully created.')
    @api.response(409, 'Role already exists.')
    @token_required
    @api.doc('create a new role')
    def post(self):
        """Creates a new Role or update an existing one """
        data = request.json
        result = create_update_role(data=data)
        return result


@api.route('/<role_name>')
@api.param('role_name', 'The UserRole name')
@api.response(200, 'Success')
@api.response(404, 'Role not found.')
@api.response(400, 'Assigned roles can not be deleted')
class UserRole(Resource):
    @api.doc('delete a role')
    @token_required
    @api.marshal_with(_user_role)
    def delete(self, role_name):
        """Delete a role given its name"""
        response, code = delete_role(role_name)
        if code != 200:
            api.abort(code, response)
        else:
            return response
