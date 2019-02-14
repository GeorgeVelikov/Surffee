from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib import messages

from .models import Survey, Question
from .forms.users import ResearcherCreationForm
from .forms.surveys import ResearcherCreateSurvey, ResearcherCreateQuestion, QuestionFormSet, ChoiceFormSet


def index(request):
    template = 'surveys/index.html'
    surveys = None
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    if request.user.is_superuser:
        surveys = Survey.objects.all
    elif request.user.is_authenticated:
        surveys = Survey.objects.filter(creator=request.user)
    context = {'surveys': surveys}
    return render(request, template, context)


def results(survey_id):
    template = 'surveys/results.html'
    survey = Survey.objects.get(pk=survey_id)
    context = {'survey': survey}
    return render(survey_id, template, context)


def detail(request, survey_id):
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    template = 'surveys/detail.html'
    survey = Survey.objects.filter(pk=survey_id)[0]
    if survey.creator != request.user and not request.user.is_superuser:
        raise PermissionDenied("You have tried to access " + survey.name + ". To gain permissions please contact "
                               + survey.creator.email + ".")
    context = {'survey': survey}
    return render(request, template, context)


def active(request):
    active_surveys = None
    template = 'surveys/active.html'
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in.")
    if request.user.is_superuser:
        active_surveys = Survey.objects.filter(active=True)
    elif request.user.is_authenticated:
        active_surveys = Survey.objects.filter(creator=request.user, active=True)
    context = {'active_surveys': active_surveys}
    return render(request, template, context)


def inactive(request):
    inactive_surveys = None
    template = 'surveys/inactive.html'
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in.")
    if request.user.is_superuser:
        inactive_surveys = Survey.objects.filter(active=False)
    elif request.user.is_authenticated:
        inactive_surveys = Survey.objects.filter(creator=request.user, active=False)
    context = {'inactive_surveys': inactive_surveys}
    return render(request, template, context)
"""
class AddQuestion(CreateView):
    template = 'surveys/add_question.html'
    model = Question
    survey = Survey.objects.get(pk=survey_id)

    # TODO: find a way to pass survey_id from survey detail. Then set it as a value in Survey: field of newly created
    # question
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.survey = request.survey_id
        return self.render_to_response(self.get_context_data(form=form))
"""


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


""" Errors """


def handler403(request, exception):
    context = {'message': exception.args[0]}  # this is the error message called with the exception
    return render(request, 'errors/403.html', context, status=403)


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CreateSurvey(CreateView):
    template_name = 'surveys/old_create.html'
    model = Survey
    form_class = ResearcherCreateSurvey
    success_url = '/'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        question_form = QuestionFormSet
        choice_form = ChoiceFormSet
        return self.render_to_response(
            self.get_context_data(form=form,
                                  question_form=question_form,
                                  choice_form=choice_form)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        question_form = QuestionFormSet(self.request.POST)
        choice_form = ChoiceFormSet(self.request.POST)
        if form.is_valid() and question_form.is_valid() and choice_form.is_valid():
            return self.form_valid(form, question_form, choice_form)
        else:
            return self.form_invalid(form, question_form, choice_form)

    def form_valid(self, form, question_form, choice_form):
        self.object = form.save()
        question_form.instance = self.object
        question_form.save()
        choice_form.instance = self.object
        choice_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, question_form, choice_form):
        return self.render_to_response(
            self.get_context_data(form=form,
                                  question_form=question_form,
                                  choice_form=choice_form)
        )


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
