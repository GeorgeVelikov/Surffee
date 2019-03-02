from django.db import models
from .survey import Choice


class Annotation(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    word = models.CharField(max_length=2**8)
    classifiction = models.CharField(max_length=2**6)
    color = models.CharField(max_length=2*3)  # this is in the example form of #FF00FF
