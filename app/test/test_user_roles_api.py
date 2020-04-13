from app.test.base import BaseTestCase


def register(self, role):
    return self.client.post(
        '/api/user',
        json={
            'email': "user@email.com",
            'username': "user",
            'password': "password",
            'roles': [role],
            'oauth_id': "oauth",
            'oauth_type': "GOOGLE"
        },
        content_type='application/json'
    )


def create_update_role(self, name, description, token):
    return self.client.post(
        '/api/user_role',
        json={
            'name': name,
            'description': description,
        },
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )


def delete_role(self, name, token):
    return self.client.delete(
        f'/api/user_role/{name}',
        headers={'Authorization': f'Bearer {token}'}
    )


class UserRoleResourceTest(BaseTestCase):

    def test_create_update_role(self):
        response = register(self, 'admin')
        token = response.json.get('Authorization')
        response = create_update_role(self, 'superadmin', 'admin description', token)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        response = create_update_role(self, 'admin', 'admin description updated', token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")

    def test_delete_role(self):
        response = register(self, 'admin')
        token = response.json.get('Authorization')
        response = delete_role(self, 'admin', token)
        self.assertEqual(response.status_code, 400)
        response = create_update_role(self, 'manager', 'manager description', token)
        self.assertEqual(response.status_code, 201)
        response = delete_role(self, 'manager', token)
        self.assertEqual(response.status_code, 200)

    def test_update_users_roles(self):
        response = register(self, 'admin')
        self.assertEqual(response.status_code, 201)
        token = response.json.get('Authorization')
        public_id = response.json['public_id']
        response = self.client.put(
            f'/api/user/{public_id}',
            json={
                'roles': ['admin']
            },
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['roles'], ['admin'])
        response = self.client.put(
            f'/api/user/{public_id}',
            json={
                'roles': ['manager']
            },
            content_type='application/json')
        self.assertEqual(response.status_code, 401)
