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

    def test_login_success(self):
        """
        Check if the user is redirected to index on successful login
        :return:
        """
        resp = self.client.post(reverse('login'), {
            'username': 'user',
            'password': 'password',
        },
                                follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('_auth_user_id', self.client.session)     # this checks if client is logged in

class IndexTests(TestCase):

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
