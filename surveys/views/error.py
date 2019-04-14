from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from ..models.answer import SurveyAnswer
from .helper import get_ip

# TODO: add redirect message to permissions


def handler403(request, exception):
    context = {'message': exception.args[0]}  # this is the error message called with the exception
    return render(request, 'errors/403.html', context, status=403)


def permission_user_logged_in(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("User not logged in")


def permission_user_owns_survey(request, survey):
    if not (request.user.pk == survey.creator.pk):
        raise PermissionDenied("User does not own the survey")


def permission_user_owns_annotation(request, annotation):
    if not (request.user.pk == annotation.creator.pk):
        raise PermissionDenied("User does not own the annotation")


def permission_user_owns_analysis(request, analysis):
    if not (request.user.pk == analysis.creator.pk):
        raise PermissionDenied("User does not own the analysis")


def permission_user_unique_answer(request, survey):
    if SurveyAnswer.objects.filter(ip_address=get_ip(request), survey=survey).exists():
        raise PermissionDenied("You have already answered the survey")


def permission_survey_active(survey):
    if not survey.active:
        raise PermissionDenied("Survey is not currently active")
