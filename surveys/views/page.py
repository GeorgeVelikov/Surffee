from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from ast import literal_eval
from chartit import DataPool, Chart

from ..models import *
from ..forms.users import ResearcherCreationForm


"""
* More modules will be created as the file expands *
                                                 """


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


class Results(CreateView):
    template_name = 'surveys/results.html'
    model = Survey
    form_class = ResearcherCreationForm

    def create_chart_data(self, survey):

        all_choices = Choice.objects.none()

        for question in survey.question_set.all():
            all_choices |= question.choice_set.all()

        data = DataPool(
                series=[{
                    'options': {
                        'source': survey.question_set.all(),
                        # 'legend_by': 'choice_text'
                    },
                    'terms': [
                        'choice',
                        'votes',
                        'question_text'
                    ]
                }]
            )

        return Chart(
            datasource=data,
            series_options=[{
                    'options': {
                        'type': 'column',
                        'stacking': True,
                        'stack': 0,
                        'xAxis': 0,
                        'yAxis': 0
                    },
                    'terms': {
                        'question_text': ['votes']}
            }])

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)
        cht = self.create_chart_data(survey)

        return self.render_to_response({'chart': cht})


def detail(request, survey_id):
    if not request.user.is_authenticated:  # user is not logged in
        raise PermissionDenied("User is not logged in")
    template = 'surveys/detail.html'
    survey = Survey.objects.get(pk=survey_id)

    # this converts the string representation of a list back to a list
    if survey.pi_choices:
        choices = literal_eval(survey.pi_choices)
        for i in range(len(choices)):
            choices[i] = choices[i].replace("_", " ").capitalize()
    else:
        choices = {}

    if survey.creator != request.user and not request.user.is_superuser:
        raise PermissionDenied("You have tried to access " + survey.name + ". To gain permissions please contact "
                               + survey.creator.email + ".")
    context = {'survey': survey, 'choices': choices}
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


def handler403(request, exception):
    context = {'message': exception.args[0]}  # this is the error message called with the exception
    return render(request, 'errors/403.html', context, status=403)


class SignUp(CreateView):
    form_class = ResearcherCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


'''       BACKUP
    
    def create_chart_data(self, survey):

        all_choices = Choice.objects.none()

        for question in survey.question_set.all():
            all_choices |= question.choice_set.all()

        data_ss = DataPool(
                series=[{
                    'options': {
                        'source': all_choices,
                        'categories': 'question__question_text',
                        'legend_by': 'choice_text',
                    },
                    'terms': {
                        'No. of votes': 'votes'
                    }
                }]
            )
'''