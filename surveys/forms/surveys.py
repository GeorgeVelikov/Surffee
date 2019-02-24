from django import forms
from django.forms.models import inlineformset_factory

from ..models import Survey, Question, Choice, PersonalInformation


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


class ResearcherUpdateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['']


class ResearcherCreateSurvey(forms.ModelForm):
    PERSONAL_INFORMATION_CHOICE = (
        ('age', 'Age'),
        ('sex', 'Sex'),
        ('country_of_birth', 'Country of Birth'),
        ('country_of_residence', 'Country of Residence'),
        ('sexual_orientation', 'Sexual orientation'),
        ('native_tongue', 'Native tongue'),
    )

    INFORMATION = "What would the survey research make " \
                  "use of in terms of background information"

    pi_set = forms.MultipleChoiceField(label=INFORMATION,
                                       required=False,
                                       widget=forms.CheckboxSelectMultiple(attrs={'class': ''}),
                                       choices=PERSONAL_INFORMATION_CHOICE,
                                       )

    class Meta:
        model = Survey
        exclude = []

    def save(self, commit=True):
        return super(ResearcherCreateSurvey, self).save(commit=commit)


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = ['active, creator']  # TODO: might want to exclude more stuff


class AnswerSurveyQuestionsForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['']  # TODO: might want to exclude more stuff


ChoiceFormSet = inlineformset_factory(Question,
                                      Choice,
                                      form=ResearcherCreateChoice,
                                      extra=1)
