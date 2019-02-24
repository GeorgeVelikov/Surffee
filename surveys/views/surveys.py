from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from ..models import Survey, Question, Choice, Researcher
from ..forms.surveys import ResearcherCreateSurvey, ResearcherCreateQuestion, ResearcherUpdateQuestion, ChoiceFormSet
from ..forms.surveys import AnswerSurveyQuestionsForm, PersonalInformationForm


class CreateNewSurvey(UpdateView):
    template_name = 'surveys/create_survey.html'
    model = Survey
    form_class = ResearcherCreateSurvey

    # can just increment id of the last survey
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        request.POST._mutable = True
        form.data['creator'] = request.user.pk
        # currently saves the PI we want in the shape of a list which is translated to a string, fix this later w/ eval
        form.data['pi_choices'] = request.POST.getlist('pi_set')
        request.POST._mutable = False

        print(form.data)
        # TODO: figure out how to save pi_set to an existing model

        if form.is_valid():
            return self.form_valid(form, request)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request):
        self.object = form.save(commit=True)
        return redirect('/surveys/inactive')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class CreateQuestion(CreateView):
    template_name = 'surveys/add_question.html'
    model = Question
    form_class = ResearcherCreateQuestion

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        choice_form = ChoiceFormSet
        return self.render_to_response(
            self.get_context_data(form=form,
                                  choice_form=choice_form,
                                  survey=survey)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet(self.request.POST)
        if form.is_valid() and choice_form.is_valid():
            return self.form_valid(form, choice_form)
        else:
            return self.form_invalid(form, choice_form)

    def form_valid(self, form, choice_form):
        self.object = form.save()
        choice_form.instance = self.object
        choice_form.save()
        return redirect('../add_question/')

    def form_invalid(self, form, choice_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  choice_form=choice_form)
        )


class EditQuestion(UpdateView):
    template_name = 'surveys/edit_question.html'
    model = Question
    form_class = ResearcherCreateQuestion

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        question_id = self.kwargs.get('question_id')

        survey = Survey.objects.get(pk=survey_id)
        question = Question.objects.get(pk=question_id)

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
        choice_set = Choice.objects.select_related().filter(question_id=question_id)

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

        if len(choice_form) == len(choices):
            for x in range(len(choices)):
                choice = Choice.objects.get(id=choices[x].id)
                choice.question = question
                choice.choice_text = (choice_form[x]["choice_text"]).value()
                choice.save()
                # TODO: choice_form[x]["DELETE"] needs to be altered, it's a checkbox

        self.object = form.save()

        return redirect('../')

    def form_invalid(self, form, choice_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  choice_form=choice_form)
        )


class ResearchAgreement(UpdateView):
    template_name = 'surveys/answer_research_agreement.html'
    model = Survey
    form_class = PersonalInformationForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  survey=survey, )
        )


class AnswerSurveyQuestions(UpdateView):
    template_name = 'surveys/answer_survey.html'
    model = Question
    form_class = AnswerSurveyQuestionsForm

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        question_id = self.kwargs.get('question_id')
        survey = Survey.objects.get(pk=survey_id)
        question = Question.objects.get(pk=question_id)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choice_form = ChoiceFormSet
        return self.render_to_response(self.get_context_data(form=form,
                                                             choice_form=choice_form,
                                                             question=question,
                                                             survey=survey
                                                             ))
