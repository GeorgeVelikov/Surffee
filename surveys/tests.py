from django.test import TestCase
from django.urls import reverse
from django.test import Client

from .models.user import Researcher

""" 
    setUp(self) works similarly to __init__, 
    it sets up the testing environment   
                                        """


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
        response = self.client.get(reverse('surveys:index'), follow=True)

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
        response = self.client.get(reverse('surveys:create'), follow=True)
        self.assertEqual(response.status_code, 200)
