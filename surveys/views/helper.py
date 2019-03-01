from django.core.exceptions import PermissionDenied
from ..models import SurveyAnswer


def get_ip(request):
    # grab ip address of person
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = None

    if forwarded_for:
        ip = forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def permission_user_logged_in(request):
    # TODO: add redirect message
    if not request.user.is_authenticated:
        return PermissionDenied("User not logged in")


def permission_user_owns_survey(request, survey):
    # TODO: add redirect message
    if not (request.user.username == str(survey.creator)):
        raise PermissionDenied("User does not own the survey")


def permission_user_unique_answer(request, survey):
    if SurveyAnswer.objects.filter(ip_address=get_ip(request), survey=survey).exists():
        return PermissionDenied("You have already answered the survey")
