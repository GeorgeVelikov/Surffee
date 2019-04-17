from django.test import TestCase
from django.urls import reverse
from django.test import Client

from ..models.user import Researcher
from ..models.survey import Survey

from .static_test import create_survey


# Test suite for creating a new survey
class CreateSurveyTests(TestCase):

    def add_survey_details(self, name, desc):
        return self.client.post(reverse('surveys:create'), {
            'name': name,
            'description': desc,
        }, follow=True)

    def add_survey_details_with_pi(self, name, desc, pi):
        return self.client.post(reverse('surveys:create'), {
            'name': name,
            'description': desc,
            'pi_set': pi,
        }, follow=True)

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(
            username='TestUser',
            password='TestPassword123456',
            email='test_create_user@mytest.com',
            is_staff=False,
            is_superuser=False
        )
        self.user.save()
        create_survey('Test Duplicate', self.user, False)

    def tearDown(self):
        Researcher.objects.get(
            username=self.user.username
        ).delete()

    def test_create_survey_template(self):
        """
        Check if the create page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('surveys:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'surveys/create_survey.html')

    def test_create_survey_without_pi_choices(self):
        """
         Check if survey gets properly created from user interface
        :return:
        """
        sur_name = 'Test Survey for Surffee'
        sur_desc = 'This survey is meant to test Surffee\'s functionality'

        self.client.force_login(self.user)
        self.add_survey_details(sur_name, sur_desc)

        sur = Survey.objects.filter(name=sur_name, creator=self.user)
        self.assertEqual(1, len(sur))   # check if only one instance of the survey is stored
        sur = sur[0]
        self.assertEqual(sur_desc, sur.description)
        self.assertEqual(False, sur.active)
        self.assertEqual('', sur.pi_choices)

        self.client.logout()

    def test_create_survey_with_pi_choices(self):
        """
         Check if surveys with any number of pi_choices gets created
        :return:
        """
        sur_name = 'test_survey_with_pi'
        pi = ['age', 'sex', 'country_of_birth', 'country_of_residence', 'sexual_orientation', 'native_tongue']

        self.client.force_login(self.user)
        for x in range(len(pi)):
            self.add_survey_details_with_pi(sur_name, 'arbitrary', pi[:x+1])

        surveys = Survey.objects.filter(creator=self.user, name=sur_name)
        self.assertEqual(len(pi), len(surveys))

    def test_create_survey_with_duplicate_name(self):
        """
         Check if user can create two surveys with the same name
        :return:
        """
        sur_name = 'Test Duplicate'
        sur_desc = 'In the end of the test there should be two surveys with the name above'

        self.client.force_login(self.user)
        self.add_survey_details(sur_name, sur_desc)
        surveys = Survey.objects.filter(name=sur_name, creator=self.user)
        self.assertEqual(2, len(surveys), msg=str(surveys))

        descs = [d.description for d in surveys]
        self.assertIn('', descs)
        self.assertIn(sur_desc, descs)

    def test_create_survey_with_empty_name(self):
        """
         Check if user can create a survey without a name
        :return:
        """
        self.client.force_login(self.user)
        users_surveys1 = len(Survey.objects.filter(creator=self.user))
        self.add_survey_details('', 'desc')
        users_surveys2 = len(Survey.objects.filter(creator=self.user))

        self.assertEqual(users_surveys1, users_surveys2, msg=Survey.objects.filter(creator=self.user))
