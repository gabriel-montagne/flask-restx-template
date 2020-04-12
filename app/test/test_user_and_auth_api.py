from app.test.base import BaseTestCase, create_test_users


def register(self):
    return self.client.post(
        '/api/user',
        json={
            'email': "user@email.com",
            'username': "user",
            'password': "password",
            'roles': ['user'],
            'oauth_id': "oauth",
            'oauth_type': "GOOGLE"
        },
        content_type='application/json')


def login(self):
    return self.client.post(
        '/api/auth/login',
        json={
            'email': "user@email.com",
            'password': "password",
        },
        content_type='application/json'
    )


def logout(self, token):
    return self.client.post(
        '/api/auth/logout',
        headers={'Authorization': f'Bearer {token}'},
        content_type='application/json'
    )


class UserResourceTest(BaseTestCase):

    def test_register_user(self):
        response = register(self)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], "application/json")

    def test_login_user(self):
        response = register(self)
        self.assertEqual(response.status_code, 201)
        response = login(self)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json.get('Authorization'))

    def test_logout_user(self):
        response = register(self)
        self.assertEqual(response.status_code, 201)
        response = login(self)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json.get('Authorization'))
        token = response.json.get('Authorization')
        response = logout(self, token)
        self.assertEqual(response.status_code, 200)

    def test_get_all_users(self):
        response = register(self)
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json.get('Authorization'))
        token = response.json.get('Authorization')
        create_test_users(5)
        response = self.client.get('/api/user',
                                   headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        self.assertEqual(len(response.json.get('users', [])), 6)
