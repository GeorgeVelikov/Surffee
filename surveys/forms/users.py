from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..models import Researcher


class ResearcherCreationForm(UserCreationForm):
    """
    * Form to create a Researcher type user
    *
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ResearcherCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

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
    """
    * Form to change the Researcher type user's password
    *
    """
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
