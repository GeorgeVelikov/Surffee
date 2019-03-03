from django.test import TestCase
from django.urls import reverse
from django.test import Client

from .models.user import Researcher

""" 
    setUp(self) works similarly to __init__, 
    it sets up the testing environment   
                                        """


class LoginTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(
            username='user',
            password="password"
        )
        self.superuser = Researcher.objects.create_superuser(
            username='superuser',
            password='password',
            email=None,
            is_staff=True,          # not sure if this is redundant, if we already make him a superuser
            is_superuser=True
        )

        self.user.save()
        self.superuser.save()

    """ helper method: login with username and password"""
    def login_response(self, username, password):
        return self.client.post(reverse('login'), {
            'username': username,
            'password': password,
        },
                                follow=True)

    def test_login_success(self):
        """
         Check if user can log in
         :return:
        """
        resp = self.login_response('user', 'password')
        self.assertRedirects(resp, reverse('home'))
        self.assertIn('_auth_user_id', self.client.session)
        self.client.logout()

    def test_login_wrong_password(self):
        """
        Check if user can log in with wrong password
        :return:
        """
        resp = self.login_response('user', 'not_the_password')
        self.assertTemplateUsed(resp, 'registration/login.html')
        self.assertNotIn('auth_user_id', self.client.session)
        # This didn't work for some reason, the resp's chain of redirects is empty in this case
        # self.assertRedirects(resp, reverse('login'), status_code=200)
        self.client.logout()

    def test_login_empty_input(self):
        """
         Check if user can log in with no username and password
        :return:
        """
        self.login_response('', '')
        self.assertNotIn('auth_user_id', self.client.session)


class HomeViewTests(TestCase):

    def test_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class IndexViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(
            username='user',
            password="password"
        )
        self.superuser = Researcher.objects.create_superuser(
            username='superuser',
            password='password',
            email=None,
            is_staff=True,          # not sure if this is redundant, if we already make him a superuser
            is_superuser=True
        )

        self.user.save()
        self.superuser.save()

    def test_index_status(self):
        """
        Check if the index page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('surveys:index'))
        self.assertEqual(response.status_code, 200)


class CreateViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(
            username='user',
            password="password"
        )
        self.superuser = Researcher.objects.create_superuser(
            username='superuser',
            password='password',
            email=None,
            is_staff=True,          # not sure if this is redundant, if we already make him a superuser
            is_superuser=True
        )

        self.user.save()
        self.superuser.save()

    def test_create_status(self):
        """
        Check if the create page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('surveys:create'))
        self.assertEqual(response.status_code, 200)
