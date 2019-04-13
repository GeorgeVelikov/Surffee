from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey, Choice, Question

from ..error import permission_user_logged_in, permission_user_owns_survey


class Delete(UpdateView):
    model = Survey

    def get(self, request, *args, **kwargs):
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, survey)

        questions = Question.objects.filter(survey=survey)
        choices = Choice.objects.filter(question__in=questions)

        choices.delete()
        questions.delete()
        survey.delete()
        return redirect('/surveys/')
