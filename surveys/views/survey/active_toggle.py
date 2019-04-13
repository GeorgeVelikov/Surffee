from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey

from ..error import permission_user_logged_in, permission_user_owns_survey


class ActiveToggle(UpdateView):
    model = Survey

    def get(self, request, *args, **kwargs):
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, survey)

        if survey.active:
            survey.active = False
        else:
            survey.active = True

        survey.save()
        return redirect('/surveys/' + str(survey_id))
