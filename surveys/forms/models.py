from django import forms
from django.forms.models import inlineformset_factory

from ..models import Survey, Question, Choice


class ResearcherCreateChoice(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['']


class ResearcherCreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['']


class ResearcherCreateSurvey(forms.ModelForm):
    class Meta:
        model = Survey
        exclude = ['']


QuestionFormSet = inlineformset_factory(Survey, Question, form=ResearcherCreateQuestion)
ChoiceFormSet = inlineformset_factory(Question, Choice, form=ResearcherCreateChoice)

