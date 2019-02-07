import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Survey, Question, Choice


class IndexViewTests(TestCase):

    def test_index_status(self):
        """
        Check if the index page is being displayed
        """
        response = self.client.get(reverse('surveys:index'))
        self.assertEqual(response.status_code, 200)


class CreateViewTests(TestCase):

    def test_create_status(self):

        response = self.client.get(reverse('surveys:create'))
        self.assertEqual(response.status_code, 200)


