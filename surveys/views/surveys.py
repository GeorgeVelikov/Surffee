from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from ..models import Survey, Question, Choice, PersonalInformation, SurveyAnswer
from ..forms.surveys import ResearcherCreateSurvey, ResearcherCreateQuestion, ResearcherUpdateQuestion, ChoiceFormSet
from ..forms.surveys import AnswerSurveyQuestionsForm, PersonalInformationForm, UpdateChoiceData

from ast import literal_eval


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

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
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
        survey_id = self.kwargs.get('survey_id')
        return redirect('../')

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


class DeleteQuestion(UpdateView):
    model = Question

    def get(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        question = Question.objects.get(pk=question_id)
        question.delete()
        return redirect('../')


class ResearchAgreement(UpdateView):
    template_name = 'surveys/answer_research_agreement.html'
    model = PersonalInformation
    form_class = PersonalInformationForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        self.clean_form(form, survey)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  survey=survey,
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        self.clean_form(form, survey)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=True)
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        question = Question.objects.filter(survey=survey)
        # create an answer that connects the pi questions answers with the survey answers
        answer_instance = SurveyAnswer.objects.create(survey=survey, pi_questions=self.object)
        return redirect('/surveys/answer/'+str(answer_instance.id)+'/question/'+str(question.first().id))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def clean_form(self, form, survey):
        # grab the actual pi-choices from the researcher as a py list
        if survey.pi_choices:
            pi_choices = literal_eval(survey.pi_choices)
        else:
            pi_choices = []

        # get all fields that are not selected by the researcher to use for the survey and save them in a list
        fields = []
        for ff in form.fields:
            if ff not in pi_choices:
                fields.append(ff)

        # iterate over list of fields and pop them, this is done because form.fields complains if we do this iteratively
        for f in fields:
            form.fields.pop(f)


class AnswerSurveyQuestions(UpdateView):
    template_name = 'surveys/answer_survey.html'
    model = Choice
    form_class = AnswerSurveyQuestionsForm

    def get(self, request, *args, **kwargs):
        self.object = None
        # grab the objects we might need
        answer_survey_id = self.kwargs.get('survey_answer_id')
        survey_answer = SurveyAnswer.objects.get(pk=answer_survey_id)

        question_id = self.kwargs.get('question_id')
        question = Question.objects.get(pk=question_id)

        choice_set = Choice.objects.filter(question=question)
        return self.render_to_response(
            self.get_context_data(question=question,
                                  survey_answer=survey_answer,
                                  choice_set=choice_set,
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        choices = request.POST.getlist('choices')
        for ch in choices:
            choice = Choice.objects.get(pk=ch)
            choice.votes += 1
            choice.save()
        return redirect('/well_this_is_being_worked_on')
