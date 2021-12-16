from django.test import TestCase, Client
from django.contrib.auth.models import User


# Create your tests here.
class UserProfileTestCase(TestCase):
    def setUp(self):
        # User.objects.create_user(username='adrenalin', password='1adrenalin3')
        self.client = Client()

    def test_reg(self):
        resp = self.client.post('account/registration', data={'email': 'adds@asd.ru', 'username': 'adrenalin',
                                                              'password': 'adrenalin123', 'firstname': 'Василий',
                                                              'lastname': 'Ретровчи'})
        print(type(resp))
        self.assertEqual(resp.status_code, 200)