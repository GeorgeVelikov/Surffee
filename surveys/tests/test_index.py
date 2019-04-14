from django.test import TestCase
from django.urls import reverse
from django.test import Client

from ..models.user import Researcher
from ..models.survey import Survey

from .static_test import create_survey


# Test suite for the app's index view
class IndexViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(
            username='TestUser',
            password='TestPassword123456',
            email='test_index_user@mytest.com',
            is_staff=False,
            is_superuser=False
        )
        self.superuser = Researcher.objects.create_superuser(
            username='superuser',
            password='TestPassword123456',
            email='test_index_superuser@mytest.com',
            is_staff=True,
            is_superuser=True
        )

        self.user.save()
        self.superuser.save()

    def tearDown(self):
        Researcher.objects.get(
            username=self.user.username
        ).delete()
        Researcher.objects.get(
            username=self.superuser.username
        ).delete()

    def test_index_template(self):
        """
        Check if the index page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'surveys/index.html')

    def test_index_with_surveys(self):
        """
         Test if existing surveys are being displayed
        :return:
        """
        active_s = create_survey("Active Survey",
                                 self.user,
                                 active=True,
                                 commit=True)
        inactive_s = create_survey("Inactive Survey",
                                   self.user,
                                   active=False,
                                   commit=True)

        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:index'))
        self.assertIn(active_s, resp.context['my_active_surveys'])
        self.assertIn(inactive_s, resp.context['my_inactive_surveys'])

    def test_index_with_surveys_from_different_users(self):
        """
         Test if the user can see other users' surveys
        :return:
        """
        users_s = create_survey("User's Survey", self.user)
        superusers_s = create_survey("Superuser's Survey", self.superuser)

        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:index'))
        self.assertIn(users_s, resp.context['my_active_surveys'])
        self.assertNotIn(superusers_s, resp.context['my_active_surveys'])

    def test_index_without_surveys(self):
        """
         Test if no surveys are being displayed when none exist
        :return:
        """

        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:index'))
        self.assertQuerysetEqual(Survey.objects.none(), resp.context['my_active_surveys'])
        self.assertQuerysetEqual(Survey.objects.none(), resp.context['my_inactive_surveys'])
