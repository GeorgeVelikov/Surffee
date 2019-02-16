from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from ..models import Survey, Question
from ..forms.users import ResearcherCreationForm


"""
* More modules will be created as the file expands *
                                                 """


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


def results(survey_id):
    template = 'surveys/results.html'
    survey = Survey.objects.get(pk=survey_id)
    context = {'survey': survey}
    return render(survey_id, template, context)


def detail(request, survey_id):
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    template = 'surveys/detail.html'
    survey = Survey.objects.filter(pk=survey_id)[0]
    if survey.creator != request.user and not request.user.is_superuser:
        raise PermissionDenied("You have tried to access " + survey.name + ". To gain permissions please contact "
                               + survey.creator.email + ".")
    context = {'survey': survey}
    return render(request, template, context)


def active(request):
    active_surveys = None
    template = 'surveys/active.html'
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in.")
    if request.user.is_superuser:
        active_surveys = Survey.objects.filter(active=True)
    elif request.user.is_authenticated:
        active_surveys = Survey.objects.filter(creator=request.user, active=True)
    context = {'active_surveys': active_surveys}
    return render(request, template, context)


def inactive(request):
    inactive_surveys = None
    template = 'surveys/inactive.html'
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in.")
    if request.user.is_superuser:
        inactive_surveys = Survey.objects.filter(active=False)
    elif request.user.is_authenticated:
        inactive_surveys = Survey.objects.filter(creator=request.user, active=False)
    context = {'inactive_surveys': inactive_surveys}
    return render(request, template, context)


def handler403(request, exception):
    context = {'message': exception.args[0]}  # this is the error message called with the exception
    return render(request, 'errors/403.html', context, status=403)


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

