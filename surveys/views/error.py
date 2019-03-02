from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from ..models.answer import SurveyAnswer


def handler403(request, exception):
    context = {'message': exception.args[0]}  # this is the error message called with the exception
    return render(request, 'errors/403.html', context, status=403)


def permission_user_logged_in(request):
    # TODO: add redirect message
    if not request.user.is_authenticated:
        raise PermissionDenied("User not logged in")


def permission_user_owns_survey(request, survey):
    # TODO: add redirect message
    if not (request.user.username == str(survey.creator)):
        raise PermissionDenied("User does not own the survey")


def permission_user_unique_answer(request, survey):
    # TODO: add redirect message
    if SurveyAnswer.objects.filter(ip_address=get_ip(request), survey=survey).exists():
        raise PermissionDenied("You have already answered the survey")
