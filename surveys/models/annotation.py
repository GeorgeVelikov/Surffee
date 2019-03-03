from django.db import models
from .survey import Survey


class Word(models.Model):
    text = models.CharField(max_length=2**6)  # limit word length to 64, because why would you need more
    classification = models.CharField(max_length=2**6)  # name of word group, decided by researcher
    color = models.CharField(max_length=2**3)  # this is in the example form of #FF00FF


class Annotation(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    words = models.ManyToManyField(Word, default=0)
