from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from ..models import Survey, Question, Choice
from ..forms.surveys import ResearcherCreateSurvey, ResearcherCreateQuestion, ChoiceFormSet
from ..forms.surveys import AnswerSurveyQuestionsForm, PersonalInformationForm


class CreateNewSurvey(CreateView):
    template = 'surveys/create.html'
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
        if form.is_valid():
            self.object = form.save()
            # this is probably dirty as heck because I've only seen form_valid() called here,
            # which is also an method overriding the superclass, so it's probably important
            messages.add_message(request, messages.INFO, "Survey created successfully")
            return redirect('../' + str(self.object.id))
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

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

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        choice_form = ChoiceFormSet
        return self.render_to_response(
            self.get_context_data(form=form,
                                  question=question,
                                  choice_form=choice_form,
                                  survey=survey,
                                  choices=choices)
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
        question_id = self.kwargs.get('question_id')

        form.id = question_id
        self.object = form.save()
        # TODO: THIS IS THE NEW QUESTION ID BUT IT ACTUALLY APPENDS IT
        self.object.id = question_id

        print(self.object.id)
        # -------------------------------------------
        choice_form.instance = self.object
        choice_form.save()
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
