import datetime

from django.test import TestCase
from django.urls import reverse
from  django.utils import timezone

from .models import Survey, Question, Choice


class ViewTests(TestCase):

    def test_status(self):
        """
        Check
        :return:
        """
        response = self.client.get(reverse('surveys:index'))
        self.assertEqual(response.status_code, 200)
