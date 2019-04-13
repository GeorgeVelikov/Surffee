from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Question

from ..error import permission_user_logged_in, permission_user_owns_survey


class Delete(UpdateView):
    model = Question

    def get(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = Question.objects.get(pk=question_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, question.survey)

        question.delete()
        return redirect('../')
