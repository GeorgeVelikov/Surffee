from django.test import TestCase
from django.urls import reverse

from ..models.user import Researcher


# Test suite for registration (signup)
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
        self.assertNotIn(email, [user.email for user in Researcher.objects.all()])

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
