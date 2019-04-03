from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField

from .user import Researcher


class Survey(models.Model):
    creator = models.ForeignKey(Researcher, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=2**8)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    description = models.CharField(max_length=2**10)
    active = models.BooleanField(default=False)
    pi_choices = models.TextField(blank=True, null=True)
    active_annotation = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"


class PersonalInformation(models.Model):
    SEX_CHOICE = (
        ('prefer not to say', 'Prefer not to say'),
        ('male', 'Male'),
        ('female', 'Female'),
    )

    # minors cannot give consent
    age = models.IntegerField(default=18, validators=[MaxValueValidator(100), MinValueValidator(18)])
    sex = models.CharField(max_length=2*6, choices=SEX_CHOICE, default='(select sex)')
    country_of_birth = CountryField(blank_label='(select country)')
    country_of_residence = CountryField(blank_label='(select country)')
    sexual_orientation = models.CharField(max_length=2**8)
    native_tongue = models.CharField(max_length=2**8)
    # TODO: add more presets for researchers to choose


class Question(models.Model):
    QUESTION_TYPES = (
        ('S', 'Single choice'),
        ('M', 'Multiple choices'),
        ('T', 'Text answer'),
        ('G', 'Gradient answer'),
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=2**8)
    # pub_date = models.DateTimeField('date published')
    type = models.CharField(choices=QUESTION_TYPES, max_length=1, default=0)

    def __str__(self): return self.question_text

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField('number of votes', default=0)

    def __str__(self): return self.choice_text

    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"
