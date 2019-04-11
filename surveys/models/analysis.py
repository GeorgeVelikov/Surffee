from django.db import models

from .annotation import Annotation
from .survey import Survey


class Analysis(models.Model):
    name = models.CharField()  # name of word group, decided by researcher
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)
    # this is the js "instance" variables
    terms = models.CharField()
    constraints = models.CharField()
