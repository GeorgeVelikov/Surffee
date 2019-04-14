from django.test import TestCase
from django.urls import reverse
from django.test import Client

from ..models.user import Researcher


# Test suite for logging in
class LoginViewTests(TestCase):

    """ helper method: login with username and password """
    def login_response(self, username, password):
        return self.client.post(reverse('login'), {
            'username': username,
            'password': password,
        },  follow=True)

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(username='TestUser',
                                                   password='TestPassword123456',
                                                   email='test_login_user@mytest.com',
                                                   is_staff=False,
                                                   is_superuser=False
                                                   )
        self.user.save()

    def tearDown(self):
        name = self.user.username
        Researcher.objects.get(username=name).delete()

    def test_login_template(self):
        """
         Check if appropriate template is being displayed
        :return:
        """
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/login.html')

    def test_login_success(self):
        """
         Check if user can log in
         :return:
        """
        username = 'TestUser'
        password = 'TestPassword123456'

        resp = self.login_response(username, password)
        self.assertRedirects(resp, reverse('home'))
        self.assertIn('_auth_user_id', self.client.session)
        self.client.logout()

    def test_login_without_username(self):
        """
         Check if user can log in with no username
        :return:
        """
        username = ''
        password = ''

        self.login_response(username, password)
        self.assertNotIn('auth_user_id', self.client.session)

    def test_login_without_password(self):
        """
         Check if user can log in with no password
        :return:
        """
        username = 'TestUser'
        password = ''

        self.login_response(username, password)
        self.assertNotIn('auth_user_id', self.client.session)

    def test_login_without_login_and_password(self):
        """
         Check if user can log in with no login and password
        :return:
        """
        username = ''
        password = ''

        self.login_response(username, password)
        self.assertNotIn('auth_user_id', self.client.session)

    def test_login_wrong_password(self):
        """
        Check if user can log in with wrong password
        :return:
        """
        username = 'TestUser'
        password = 'wrong_password'

        self.login_response(username, password)
        self.assertNotIn('auth_user_id', self.client.session)
        self.client.logout()
