from django.test import TestCase
from django.urls import reverse
from django.test import Client

from ..models.user import Researcher
from ..models.survey import Survey

from .static_test import create_survey


# Test suite for adding question to an existing survey
class AddQuestionTests(TestCase):

    def add_question(self, q_text, choices=None, t='S'):
        context = self.default_context
        context['question_text'] = q_text
        context['type'] = t
        if choices is not None:
            context.update(choices)
            context['choice_set-TOTAL_FORMS'] = len(choices)

        return self.client.post(
            reverse(
                'surveys:add_question',
                args=(self.sur.id,)
            ),
            context,
            follow=True)

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

        sur_name = 'Survey to test question addition etc.'
        create_survey(sur_name, self.user, False)
        self.sur = Survey.objects.get(name=sur_name)
        self.default_context = {
            'survey': self.sur.id,
            'q_text': 'default',
            'choice_set-TOTAL_FORMS': 0,
            'choice_set-INITIAL_FORMS': 0,
            'choice_set-MIN_NUM_FORMS': 0,
            'choice_set-MAX_NUM_FORMS': 1000,
            'type': 'S',
        }

    def test_add_question_status(self):
        """
        Check if the question adding page is being displayed
        :return:
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('surveys:add_question', args=(self.sur.id,)))
        self.assertEqual(response.status_code, 200)

    def test_add_question_no_question_text(self):
        """
         Check if user can create a question with no question text
        :return:
        """
        q_text = ''
        self.client.force_login(self.user)
        self.add_question(q_text)
        questions = [str(x) for x in self.sur.question_set.all()]
        self.assertNotIn(q_text, questions)

    def test_add_question_no_answers(self):
        """
         Check if user can create a question with no answers
        :return:
        """
        q_text = 'Question text'
        self.client.force_login(self.user)
        self.add_question(q_text)
        questions = [str(x) for x in self.sur.question_set.all()]
        self.assertIn(q_text, questions)

    def test_add_question_with_ten_answers(self):
        """
         Check if question is added properly with moderate amount of answer choices provided
        name of choice fields: choice_set-<id of field>-choice_text
        :return:
        """
        self.client.force_login(self.user)
        q_text = "This question contains 10 choices"
        c_text = "Choice%d"
        choices = {}
        for x in range(10):
            key = "choice_set-%d-choice_text" % x
            choices[key] = c_text % x

        self.add_question(q_text, choices)
        questions = [str(x) for x in self.sur.question_set.all()]
        self.assertIn(q_text, questions)
        question = self.sur.question_set.get(question_text=q_text)
        self.assertEqual(10, len(question.choice_set.all()), msg=str(question.choice_set.all()))
        choice_texts = [str(x) for x in question.choice_set.all()]
        for key in choices:
            self.assertIn(choices[key], choice_texts)
