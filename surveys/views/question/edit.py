from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey, Question, Choice
from ...forms.surveys import ResearcherCreateQuestion, ResearcherUpdateQuestion, ChoiceFormSet

from ..error import permission_user_logged_in, permission_user_owns_survey


class Edit(UpdateView):
    template_name = 'surveys/edit_question.html'
    model = Question
    form_class = ResearcherCreateQuestion

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        question_id = self.kwargs.get('question_id')

        survey = Survey.objects.get(pk=survey_id)
        question = Question.objects.get(pk=question_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, survey)

        """
            - filter grabs only the choices belonging to this question
            - values_list makes them a nicer format we can use in js
            - convert to list to remove the QuerySet at the beginning of the data type
        """
        choices = list(Choice.objects.filter(question=question_id).values_list("choice_text", flat=True))
        votes = list(Choice.objects.filter(question=question_id).values_list("votes", flat=True))

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        choice_form = ChoiceFormSet
        return self.render_to_response(
            self.get_context_data(form=form,
                                  question=question,
                                  choice_form=choice_form,
                                  survey=survey,
                                  choices=choices,
                                  votes=votes)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        question_id = self.kwargs.get('question_id')

        instance = Question.objects.get(pk=question_id)

        form = ResearcherUpdateQuestion(request.POST, instance=instance)
        choice_form = ChoiceFormSet(self.request.POST)

        if form.is_valid() and choice_form.is_valid():
            return self.form_valid(form, choice_form)
        else:
            return self.form_invalid(form, choice_form)

    def form_valid(self, form, choice_form):
        question_id = self.kwargs.get('question_id')

        question = Question.objects.get(pk=question_id)
        choices = Choice.objects.filter(question_id=question_id)

        less_fields = min(len(choice_form), len(choices))

        for x in range(less_fields):
            choice = Choice.objects.get(id=choices[x].id)
            choice.choice_text = (choice_form[x]["choice_text"]).value()
            choice.save()

        if less_fields == len(choice_form):
            for y in range(len(choice_form), len(choices)):
                removed_choice = Choice.objects.get(id=choices[y].id)
                removed_choice.delete()

        elif less_fields == len(choices):
            for y in range(len(choices), len(choice_form)):
                new_choice_text = (choice_form[y]["choice_text"]).value()
                new_choice = Choice(question=question,
                                    choice_text=new_choice_text)
                new_choice.save()

        self.object = form.save()

        return redirect('../')

    def form_invalid(self, form, choice_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  choice_form=choice_form)
        )
