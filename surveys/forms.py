from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Researcher


class ResearcherCreationForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = Researcher
        fields = ('username', 'email', 'password', )


class ResearcherChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Researcher
        fields = ('username', 'email', 'password', )
