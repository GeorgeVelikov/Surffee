from django import forms
from django.forms.models import inlineformset_factory

from ..models.survey import Survey, Question, Choice, PersonalInformation
from ..models.annotation import Word


class ResearcherCreateChoice(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearcherCreateChoice, self).__init__(*args, **kwargs)
        self.fields['choice_text'].label = False

    class Meta:
        model = Choice
        exclude = ['votes']


class UpdateChoiceData(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['']


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
                                       widget=forms.CheckboxSelectMultiple(),
                                       choices=PERSONAL_INFORMATION_CHOICE,
                                       )
    pi_set.widget.attrs['class'] = 'pi_checkbox '

    class Meta:
        model = Survey
        exclude = []

    def save(self, commit=True):
        return super(ResearcherCreateSurvey, self).save(commit=commit)


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = ['active, creator']


class AnswerSurveyQuestionsForm(forms.ModelForm):
    class Meta:
        model = Choice
        exclude = ['']


class AnnotationWordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnotationWordForm, self).__init__(*args, **kwargs)
        self.fields['classification'].label = "Word type"
        self.fields['classification'].widget.attrs['class'] = "textinput textInput form-control"

    class Meta:
        model = Word
        exclude = ['']


ChoiceFormSet = inlineformset_factory(Question,
                                      Choice,
                                      form=ResearcherCreateChoice,
                                      extra=1)
