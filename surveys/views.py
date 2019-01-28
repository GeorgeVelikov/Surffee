from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Survey


def index(request):
    template = 'surveys/index.html'
    return render(request, template)


def results(request, survey_id):
    response = "You're looking at the results of survey %s."
    return HttpResponse(response % survey_id)

