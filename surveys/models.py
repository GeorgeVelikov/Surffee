import datetime
from django.db import models
from django.utils import timezone

QUESTION_TYPES = (
    ('S', 'Single choice'),
    ('M', 'Multiple choices'),
    ('T', 'Text answer')
)


class Survey(models.Model):
    name = models.CharField(max_length=300)
    creation_date = models.DateTimeField('date created')
    pub_date = models.DateTimeField('date published')

    def __str__(self): return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, default=0) # TODO: specify on_delete // if u delete the question, keep survey but not the choices
    question_text = models.CharField(max_length=300)
    # pub_date = models.DateTimeField('date published')
    type = models.CharField(choices=QUESTION_TYPES, max_length=1, default=0)

    def __str__(self): return self.question_text

    """
    use in surveys
        def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
    """


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField('number of votes', default=0)

    def __str__(self): return self.choice_text
