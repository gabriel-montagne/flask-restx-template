from app.main import db
from app.main.model.user import User
from app.main.model.user_roles import UserRole
from app.main.service.authorization_helper import init_role_authorization


def create_update_role(data):
    role = UserRole.query.filter_by(name=data['name']).first()
    if not role:
        new_role = UserRole(
            name=data['name'],
            description=data.get('description', ''),
            authorization=init_role_authorization(data['name'])
        )
        db.session.add(new_role)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully added.',
            'role': new_role.name
        }
        return response_object, 201
    else:
        role.description = data.get('description', role.description)
        role.authorization = data.get('authorization', role.authorization)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.',
            'role': role.name
        }
        return response_object


def delete_role(role_name):
    user_role = UserRole.query.filter_by(name=role_name).first()
    if user_role:
        user_roles = [r for u in User.query.all() for r in u.roles]
        if user_role.name not in user_roles:
            UserRole.query.filter_by(name=role_name).delete()
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': 'Role deleted',
            }
            return response_object, 200
        else:
            response_object = {
                'status': 'fail',
                'message': 'Assigned roles can not be deleted',
            }
            return response_object, 400

    else:
        response_object = {
            'status': 'fail',
            'message': 'Role does not exists',
        }
        return response_object, 401


def get_all_roles():
    return UserRole.query.all()


def get_role_by_name(name):
    return UserRole.query.filter_by(name=name).first()
