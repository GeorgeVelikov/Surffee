from django.test import TestCase
from django.urls import reverse
from django.test import Client

from .models.user import Researcher
from .models.survey import Survey

""" 
    setUp(self) works similarly to __init__, 
    it sets up the testing environment   
                                        """


def create_survey(name, creator, active=True, commit=True):
    """ Helper method to create a new survey """
    survey = Survey(name=name,
                    creator=creator,
                    active=active)
    if commit:
        survey.save()
    return survey


class SignUpViewTests(TestCase):

    """ helper method to sign up with given details """
    def signup_response(self, username, password1, password2, email):
        return self.client.post(reverse('signup'), {
            'username': username,
            'password1': password1,
            'password2': password2,
            'email': email,
        },  follow=True)

    def test_signup_template(self):
        """
         Test if appropriate template is used for the sign up view
        :return:
        """
        signup_response = self.client.get(reverse('signup'))
        self.assertEqual(signup_response.status_code, 200)
        self.assertTemplateUsed(signup_response, 'signup.html')

    def test_signup_success(self):
        """
         Test if signing up creates a new user with appropriate data
        :return:
        """
        username = 'TestUser'
        password = 'TestPassword123456'
        email = 'test_signup_success@mytest.com'

        response = self.signup_response(username, password, password, email)
        self.assertRedirects(response, reverse('login'))
        self.assertIn(username, [str(user) for user in Researcher.objects.all()])
        test_user = Researcher.objects.get(username=username)
        self.assertEqual(email, test_user.email)

    def test_signup_without_username(self):
        """
         Test if user can sign up without providing a username
        :return:
        """
        username = ''
        password = 'TestPassword123456'
        email = 'test_signup_without_username@mytest.com'

        self.signup_response(username, password, password, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_with_short_password(self):
        """
         Test if user can sign up with password shorter than 8 characters
        :return:
        """
        username = 'TestUser'
        password = 'Test'
        email = 'test_signup_with_short_password@mytest.com'

        self.signup_response(username, password, password, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_without_password1(self):
        """
         Test if user can sign up on empty password1('')
            :return:
        """
        username = "TestUser"
        password1 = ''
        password2 = 'TestPassword123456'
        email = 'test_signup_without_password1@mytest.com'

        self.signup_response(username, password1, password2, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_without_password2(self):
        """
         Test if user can sign up on empty password2('')
            :return:
        """
        username = "TestUser"
        password1 = 'TestPassword123456'
        password2 = ''
        email = 'test_signup_without_password2@mytest.com'

        self.signup_response(username, password1, password2, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_without_both_passwords(self):
        """
         Test if user can sign up on empty passwords('')
        :return:
        """
        username = "TestUser"
        password = ''
        email = 'test_signup_without_both_passwords@mytest.com'

        self.signup_response(username, password, password, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_with_unmatching_passwords(self):
        """
         Test if user can signup with the two password being different
        :return:
        """
        username = 'TestUser'
        password1 = 'TestPassword123456'
        password2 = 'PasswordTest123456'
        email = 'test_signup_with_unmatching_passwords@mytest.com'

        self.signup_response(username, password1, password2, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_without_email(self):
        """
         Test if user can sign up without providing an e-mail address
        :return:
        """
        username = 'TestUser'
        password = 'TestPassword123456'
        email = ''

        self.signup_response(username, password, password, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_signup_with_incorrect_email(self):
        """
         Test if user can sign up with wrongly formatted e-mail address
        :return:
        """
        username = 'TestUser'
        password = 'TestPassword123456'
        email = '.this.is.an!incorrect password'

        self.signup_response(username, password, password, email)
        self.assertNotIn(username, [str(user) for user in Researcher.objects.all()])

    def test_singup_with_duplicate_email(self):
        username1 = 'TestUser1'
        username2 = 'TestUser2'
        password = 'TestPassword123456'
        email = 'test_singup_with_duplicate_email@mytest.com'

        self.signup_response(username1, password, password, email)
        self.signup_response(username2, password, password, email)

        res = [str(r) for r in Researcher.objects.all()]
        self.assertIn(username1, res, msg='\n%s not signed up' % username1)
        self.assertNotIn(username2, res, msg='\n%s signed up' % username2)


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


class ActiveViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = Researcher.objects.create_user(
            username='TestUser',
            password='TestPassword123456',
            email='test_active_user@mytest.com',
            is_staff=False,
            is_superuser=False
        )
        self.superuser = Researcher.objects.create_superuser(
            username='superuser',
            password='TestPassword123456',
            email='test_active_superuser@mytest.com',
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

    def test_active_template(self):
        """
        Check if the active page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:active'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'surveys/active.html')

    def test_active_with_survey(self):
        """
         Test if existing surveys are being displayed
        :return:
        """
        active_s = create_survey("Active Survey", self.user)

        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:active'))
        self.assertIn(active_s, resp.context['active_surveys'])

    def test_active_without_survey(self):
        """
         Test if no surveys are being displayed when none exist
        :return:
        """
        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:index'))
        self.assertNotIn('active_surveys', resp.context)

    def test_active_with_surveys_from_different_users(self):
        """
         Test if the user can see other users' surveys
        :return:
        """
        users_s = create_survey("User's Survey", self.user)
        superusers_s = create_survey("Superuser's Survey", self.superuser)

        self.client.force_login(self.user)
        resp = self.client.get(reverse('surveys:active'))
        self.assertIn(users_s, resp.context['active_surveys'])
        self.assertNotIn(superusers_s, resp.context['active_surveys'])


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
        Researcher.objects.get(
            username=self.superuser.username
        ).delete()

    def test_create_survey_status(self):
        """
        Check if the create page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('surveys:create'))
        self.assertEqual(response.status_code, 200)

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


class CreateQuestionTests(TestCase):

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
        create_survey('Survey to test question addition etc.', self.user, False)
        # TODO: test adding a question, question wiht no answers, question with no text, quetsion with empty answer

    def test_create_question_status(self):
        """
        Check if the question adding page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('surveys:add_question'))
        self.assertEqual(response.status_code, 200)
