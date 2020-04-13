import unittest
from app.main.service.authorization_helper import init_role_authorization, get_merged_authorization
from app.main.model.user_roles import UserRole


user_authorization = {
    '/api/user': {'get': True, 'post': False, 'put': False, 'delete': False},
    '/api/user_role': {'get': True, 'post': False, 'put': False, 'delete': False},
    '/api/auth': {'get': True, 'post': False, 'put': False, 'delete': False}
}
admin_authorization = {
    '/api/user': {'get': True, 'post': True, 'put': True, 'delete': True},
    '/api/user_role': {'get': True, 'post': True, 'put': True, 'delete': True},
    '/api/auth': {'get': True, 'post': True, 'put': True, 'delete': True}
}


class AuthorizationServiceTestCase(unittest.TestCase):
    def test_init_authorization(self):
        manager_auth = init_role_authorization('manager')
        self.assertEqual(manager_auth, user_authorization)
        admin_auth = init_role_authorization('admin')
        self.assertEqual(admin_auth, admin_authorization)

    def test_get_user_authorization(self):
        roles = [UserRole(name=role, authorization=init_role_authorization(role)) for role in ['manager', 'admin']]
        self.assertEqual(get_merged_authorization(roles), admin_authorization)
