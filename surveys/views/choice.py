from django.shortcuts import redirect
from django.views.generic import UpdateView

from ..models import Question, Choice

from .helper import permission_user_logged_in, permission_user_owns_survey


class Delete(UpdateView):
    # TODO: fix not showing of personal data used
    model = Question

    def get(self, request, *args, **kwargs):
        choice_id = self.kwargs.get('choice_id')
        choice = Choice.objects.get(pk=choice_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, choice.question.survey)

        choice.delete()
        return redirect('../')