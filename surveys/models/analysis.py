from django.db import models

from .user import Researcher
from .annotation import Annotation
from .survey import Survey


class AnalysisSingle(models.Model):
    creator = models.ForeignKey(Researcher, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=2**8)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)

    # this is the js "instance" variables
    terms = models.CharField(max_length=2**8)
    constraints = models.CharField(max_length=2**16)


class AnalysisGraph(models.Model):
    creator = models.ForeignKey(Researcher, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=2 ** 8)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    questions_graphs = models.CharField(max_length=2**16)
