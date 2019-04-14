from django.test import TestCase
from django.urls import reverse
from django.test import Client

from ..models.user import Researcher


# Test suite for the main homepage
class HomeViewTests(TestCase):

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

    def test_home_template(self):
        """
         Check if appropriate template is being displayed
        :return:
        """
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

    def test_home_greeting_username(self):
        """
         Check if appropriate username is given at greeting
        :return:
        """
        self.client.force_login(self.user)
        resp = self.client.get(reverse('home'))
        name = resp.context['user'].username
        self.assertEqual(name, self.user.username)
