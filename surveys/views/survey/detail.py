from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from ...models.survey import Survey

from ast import literal_eval


def detail(request, survey_id):
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")

    template = 'surveys/detail.html'
    survey = Survey.objects.get(pk=survey_id)

    if survey.creator != request.user:
        raise PermissionDenied("You do not own this survey")

    # this converts the string representation of a list back to a list
    if survey.pi_choices:
        choices = literal_eval(survey.pi_choices)
        for i in range(len(choices)):
            choices[i] = choices[i].replace("_", " ").capitalize()
    else:
        choices = None

    if survey.creator != request.user and not request.user.is_superuser:
        raise PermissionDenied("You have tried to access " + survey.name + ". To gain permissions please contact "
                               + survey.creator.email + ".")
    context = {'survey': survey, 'choices': choices}
    return render(request, template, context)
