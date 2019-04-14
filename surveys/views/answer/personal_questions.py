from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey, Question, PersonalInformation
from ...models.answer import SurveyAnswer

from ...forms.surveys import PersonalInformationForm

from ..helper import get_ip
from ..error import permission_user_unique_answer, permission_survey_active

from ast import literal_eval


class ResearchAgreement(UpdateView):
    template_name = 'surveys/answer_research_agreement.html'
    model = PersonalInformation
    form_class = PersonalInformationForm

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        permission_survey_active(survey)

        if SurveyAnswer.objects.filter(ip_address=get_ip(request), survey=survey).exists():
            survey_questions = Question.objects.filter(survey=survey)
            survey_answer = SurveyAnswer.objects.get(ip_address=get_ip(request), survey=survey)
            for next_question in survey_questions:
                if next_question not in survey_answer.question.all():
                    return redirect('../question/'+str(next_question.id))
            permission_user_unique_answer(request, survey)

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.clean_form(form, survey)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  survey=survey,
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        self.clean_form(form, survey)

        ip = get_ip(request)

        if form.is_valid():
            return self.form_valid(form, ip)
        else:
            return self.form_invalid(form, ip)

    def form_valid(self, form, ip):
        self.object = form.save(commit=True)
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        question = Question.objects.filter(survey=survey)

        # create an answer instance
        SurveyAnswer.objects.create(pi_questions=self.object,
                                    survey=survey,
                                    ip_address=ip,
                                    )

        return redirect('/surveys/answer/'+str(survey_id)+'/question/'+str(question.first().id))

    def form_invalid(self, form, ip):
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
