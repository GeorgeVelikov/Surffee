from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


"""          ""
* USER MODELS *
""          """


class Researcher(AbstractUser):
    def __str__(self):
        return self.username


"""            ""
* SURVEY MODELS *
""            """


class Survey(models.Model):
    creator = models.ForeignKey(Researcher, on_delete=models.CASCADE, default=0)
    name = models.CharField(max_length=300)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    description = models.CharField(max_length=100000)
    active = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"


class Question(models.Model):
    QUESTION_TYPES = (
        ('S', 'Single choice'),
        ('M', 'Multiple choices'),
        ('T', 'Text answer')
    )
    # TODO: specify on_delete // if u delete the question, keep survey but not the choices
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=300)
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
