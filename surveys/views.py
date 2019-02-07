from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.generic import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy

from .models import Survey
from .forms import ResearcherCreationForm, ResearcherCreateSurvey


def index(request):
    template = 'surveys/index.html'
    return render(request, template)


def results(request, survey_id):
    response = "You're looking at the results of survey %s."
    return HttpResponse(response % survey_id)


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreateSurvey(CreateView):
    form_class = ResearcherCreateSurvey
    success_url = reverse_lazy('home')
    template_name = 'surveys/create.html'
