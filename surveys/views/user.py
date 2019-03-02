from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from ast import literal_eval

from ..models import *
from ..forms.users import ResearcherCreationForm


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
