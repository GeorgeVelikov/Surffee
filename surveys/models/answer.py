from django.db import models
from .survey import Survey, Question, Choice, PersonalInformation


class SurveyAnswer(models.Model):
    pi_questions = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, default=0)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, default=0)
    question = models.ManyToManyField(Question, default=0)
    choice = models.ManyToManyField(Choice, default=0)
    ip_address = models.GenericIPAddressField()
