from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey, Question, Choice
from ...models.answer import SurveyAnswer

from ...forms.surveys import AnswerSurveyQuestionsForm

from ..helper import get_ip, get_next_question
from ..error import permission_user_unique_answer


class SurveyQuestions(UpdateView):
    template_name = 'surveys/answer_survey.html'
    model = Choice
    form_class = AnswerSurveyQuestionsForm

    def get(self, request, *args, **kwargs):
        self.object = None
        # grab the objects we might need
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        survey_answer = SurveyAnswer.objects.get(ip_address=get_ip(request), survey=survey)
        question_id = self.kwargs.get('question_id')
        question = Question.objects.get(pk=question_id)

        choice_set = Choice.objects.filter(question=question)
        return self.render_to_response(
            self.get_context_data(survey=survey,
                                  question=question,
                                  survey_answer=survey_answer,
                                  choice_set=choice_set,
                                  )
        )

    def post(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = Question.objects.get(pk=question_id)
        choices = request.POST.getlist('choices')
        survey_answer = SurveyAnswer.objects.get(ip_address=get_ip(request), survey=question.survey)

        survey_answer.question.add(question)
        for ch in choices:
            choice = Choice.objects.get(pk=ch)
            survey_answer.choice.add(choice)
            choice.votes += 1
            choice.save()
        survey_answer.save()

        next_question = get_next_question(survey_answer, question)

        if not next_question:
            permission_user_unique_answer(request, question.survey)

        return redirect('../'+str(next_question.id))
