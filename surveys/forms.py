from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Researcher, Survey, Question, Choice


class ResearcherCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = Researcher
        fields = ('username', 'password1', 'password2', 'email',)
        help_texts = {
            'username': None,
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ResearcherCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ResearcherChangeForm(UserChangeForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Researcher
        fields = ('username', 'password1', 'password2', 'email', )
        help_texts = {
            'username': None,
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ResearcherChangeForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ResearcherCreateChoice(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', ]


class ResearcherCreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'type', ]


class ResearcherCreateSurvey(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['creator', 'name']

    def save(self, commit=True):
        survey = super(ResearcherCreateSurvey, self).save(commit=False)
        if commit:
            survey.save()
        return survey
