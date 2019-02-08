from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.template import loader
from django.views.generic import CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from .models import Survey
from .forms import ResearcherCreationForm, ResearcherCreateSurvey


def index(request):
    template = 'surveys/index.html'
    surveys = None
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    if request.user.is_superuser:
        surveys = Survey.objects.all
    elif request.user.is_authenticated:
        surveys = Survey.objects.filter(creator=request.user)
    context = {'surveys': surveys}
    return render(request, template, context)


def results(request, survey_id):
    response = "You're looking at the results of survey %s."
    return HttpResponse(response % survey_id)


""" Errors """


def handler403(request, exception, template_name="403.html"):
    response = render_to_response("errors/403.html")
    response.status_code = 403
    return response


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreateSurvey(CreateView):
    form_class = ResearcherCreateSurvey
    success_url = reverse_lazy('home')
    template_name = 'surveys/create.html'
