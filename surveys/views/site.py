from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from ..models.survey import Survey


def base(request):
    username = "Profile"
    surveys_active = []
    surveys_inactive = []

    if request.user.is_authenticated:
        username = request.user.username
        all_surveys = Survey.objects.filter(creator=request.user.pk)

        for survey in all_surveys:
            if survey.active:
                surveys_active.append(survey)
            else:
                surveys_inactive.append(survey)

    else:
        surveys_active = None
        surveys_inactive = None

    context = {'username': username,
               'surveys_active': surveys_active,
               'surveys_inactive': surveys_inactive,
               }

    return context


def index(request):
    template = 'surveys/index.html'
    context = {}
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    if request.user.is_authenticated:
        context['my_active_surveys'] = Survey.objects.filter(creator=request.user, active=True)
        context['my_inactive_surveys'] = Survey.objects.filter(creator=request.user, active=False)
    if request.user.is_superuser:
        context['all_active_surveys'] = Survey.objects.filter(active=True)
        context['all_inactive_surveys'] = Survey.objects.filter(active=False)
    return render(request, template, context)


def active_surveys(request):
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


def inactive_surveys(request):
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
