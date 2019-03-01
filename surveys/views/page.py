from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from ast import literal_eval

from ..models import *
from ..forms.users import ResearcherCreationForm


"""
* More modules will be created as the file expands *
                                                 """


def base(request):
    username = "Profile"
    surveys_active = []
    surveys_inactive = []

    if request.user.is_authenticated:
        username = request.user.username
        all_surveys = Survey.objects.filter(creator=request.user.pk)

        for survey in all_surveys:
            if survey.active:
                surveys_active.append(survey)
            else:
                surveys_inactive.append(survey)

    else:
        surveys_active = None
        surveys_inactive = None

    context = {'username': username,
               'surveys_active': surveys_active,
               'surveys_inactive': surveys_inactive,
               }

    return context


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

    def chart_for_each_question(self, survey):
        """ This method return a list of pairs (question_id, json_data)
            Can be easily modified later to also modify
            the size or type of chart                               """
        chart_context = []

        question_count = 1
        for question in survey.question_set.all():
            question_number = "Question " + str(question_count)
            question_text = question.question_text
            question_count += 1

            json_data = {
                "chart": None,
                "data": [],
            }

            # meta data for the chart
            chart_config = {
                "caption": question_number,
                "subcaption": question_text,
                "numbersuffix": " votes",
                "theme": "candy",
            }

            for choice in question.choice_set.all():
                json_data["data"].append({
                    "label": choice.choice_text,
                    "value": choice.votes,
                })

            json_data["chart"] = chart_config
            chart_context.append((question_number, json_data))
        return chart_context

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        context = {"charts": self.chart_for_each_question(survey)}
        return render(request, self.template_name, context)


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
        choices = None

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


    def fc(self, survey):

        # Todo: question_text might be too long, consider just using "Question1, Question2,...".
        #       Maybe cut the string if it's to long, display the cut string with elipsis
        #       and show full text on hover

        max_choices = 0
        question_text = []
        for question in survey.question_set.all():
            question_text.append({"label": question.question_text})
            choice_no = question.choice_set.all().count()
            if choice_no > max_choices:
                max_choices = choice_no

        dataset = []
        for question in survey.question_set.all():
            votes = []
            counter = max_choices
            for choice in question.choice_set.all():
                votes.append({"value": str(choice.votes)})
                counter -= 1
            if counter > 0:
                votes.extend([{"value": "0"}]*counter)

            
            dataset.append({"seriesname": question.question_text,
                            "data": votes})

        # Todo: theme fusion displays number of votes in each element of stuck, check if possible with other themes
        print("\n\n", str(dataset), "\n\n")

        return FusionCharts(            # OPTIONS
                 'stackedcolumn2d',     # specify type of chart
                 'test',                # chart's id
                 '100%',                # width
                 '200%',                # height
                 'results-chart',       # target dir
                 'json',                # data format
                                        # chart data
                 """{                    
          "chart": {
            "caption": "%(survey_name)s",
            "subcaption": "Subcaption, let's leave it here for now",
            "numbersuffix": " votes",
            "plottooltext": "<b>$dataValue</b> responded with $seriesName",
            "theme": "candy",
            "drawcrossline": "1"
          },
          "categories": [
            {
              "category": %(labels)s
            }
          ],
          "dataset": %(ds)s
        }"""
                 % {
                    'survey_name': survey.name,
                    'labels': question_text,
                    'ds': dataset
                    }
        )

'''