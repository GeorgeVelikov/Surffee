from django.db import models
from .survey import Choice
from .user import Researcher


class Annotation(models.Model):
    name = models.CharField(max_length=2**6)
    creator = models.ForeignKey(Researcher, on_delete=models.CASCADE, default=0)


class Classification(models.Model):
    name = models.CharField(max_length=2 ** 6)  # name of word group, decided by researcher
    color = models.CharField(max_length=2 ** 3)  # colour of the classification
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)


class Word(models.Model):
    text = models.CharField(max_length=2**6)  # limit word length to 64, because why would you need more
    start = models.IntegerField()
    end = models.IntegerField()
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)


