from django import forms
from django.forms.models import inlineformset_factory

from ..models import Survey, Question, Choice


class ResearcherCreateChoice(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearcherCreateChoice, self).__init__(*args, **kwargs)
        self.fields['choice_text'].label = False

    class Meta:
        model = Choice
        exclude = ['votes']


class ResearcherCreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['']


class ResearcherCreateSurvey(forms.ModelForm):
    class Meta:
        model = Survey
        exclude = ['active']


ChoiceFormSet = inlineformset_factory(Question,
                                      Choice,
                                      form=ResearcherCreateChoice,
                                      extra=1)
