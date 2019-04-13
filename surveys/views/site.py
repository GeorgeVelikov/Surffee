from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from ..models.survey import Survey
from ..models.analysis import AnalysisSingle, AnalysisGraph


def base(request):
    username = "Profile"
    surveys_active = []
    surveys_inactive = []

    all_analysis_single = None
    all_analysis_multi = None
    all_analysis_graph = None

    if request.user.is_authenticated:
        username = request.user.username
        all_surveys = Survey.objects.filter(creator=request.user.pk)
        all_analysis_single = AnalysisSingle.objects.filter(creator=request.user.pk)
        all_analysis_multi = None
        all_analysis_graph = AnalysisGraph.objects.filter(creator=request.user.pk)

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
               'all_analysis_single': all_analysis_single,
               'all_analysis_multi': all_analysis_multi,
               'all_analysis_graph': all_analysis_graph,
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


def documentation(request):
    template = 'documentation.html'
    context = {}
    return render(request, template, context)