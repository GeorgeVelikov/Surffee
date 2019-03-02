from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView

from ..models.survey import Survey
from ..forms.surveys import ResearcherCreateSurvey
from ..forms.users import ResearcherCreationForm

from .error import permission_user_logged_in, permission_user_owns_survey

from django.core.exceptions import PermissionDenied
from ast import literal_eval


class Create(UpdateView):
    template_name = 'surveys/create_survey.html'
    model = Survey
    form_class = ResearcherCreateSurvey

    # can just increment id of the last survey
    def get(self, request, *args, **kwargs):
        permission_user_logged_in(request)

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


class ActiveToggle(UpdateView):
    model = Survey

    def get(self, request, *args, **kwargs):
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, survey)

        if survey.active:
            survey.active = False
        else:
            survey.active = True

        survey.save()
        return redirect('/surveys/'+str(survey_id))


class Delete(UpdateView):
    model = Survey

    def get(self, request, *args, **kwargs):
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        permission_user_logged_in(request)
        permission_user_owns_survey(request, survey)

        survey.delete()
        return redirect('/surveys/')


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

            # choices data for the chart
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

        context = {
            "charts": self.chart_for_each_question(survey),
            "survey": survey
        }
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
