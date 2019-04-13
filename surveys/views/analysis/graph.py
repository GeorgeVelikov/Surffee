from django.shortcuts import redirect
from django.views.generic import CreateView

from surveys.models.survey import Survey, Question
from surveys.models.analysis import AnalysisGraph
from surveys.forms.analysis import AnalysisCreator

from django.core import serializers
from ast import literal_eval
from urllib import parse

from ...views.error import permission_user_owns_survey


class AnalysisGraphTerm(CreateView):
    template_name = 'analysis/graph.html'
    model = Survey
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        get_variables = request.GET

        if "analysis" in get_variables:
            analysis = AnalysisGraph.objects.get(pk=get_variables['analysis'])
            survey_id = analysis.survey.pk
            operation = "overwrite"
            analysis_name = analysis.name
            analysis_pk = analysis.pk
            questions_graphs = analysis.questions_graphs

        else:
            analysis_name = get_variables['name']
            analysis_pk = 0
            survey_id = get_variables['survey']
            operation = "save"
            questions_graphs = {}

        survey = Survey.objects.get(pk=survey_id)
        survey_name = survey.name

        permission_user_owns_survey(request, survey)

        survey_data = literal_eval(serializers.serialize("json", survey.question_set.all()))

        for m in survey_data:
            question = Question.objects.get(pk=m['pk'])
            m['fields']['choices'] = literal_eval(serializers.serialize("json", question.choice_set.all()))

        return self.render_to_response(
            self.get_context_data(form=form,
                                  survey=survey,
                                  survey_data=survey_data,
                                  operation=operation,
                                  analysis_name=analysis_name,
                                  analysis_pk=analysis_pk,
                                  survey_name=survey_name,
                                  questions_graphs=questions_graphs,
                                  )
        )

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            analysis_pk = request.POST['delete']

            analysis = AnalysisGraph.objects.get(pk=analysis_pk)

            analysis.delete()
            return redirect('./')

        else:
            terms = {}
            post_terms = parse.parse_qs(request.POST['terms'])

            for key in post_terms:
                nk = key.replace("[]", "")
                terms[nk] = post_terms[key]

            if request.POST['operation'] == "save":
                analysis_name = request.GET['name']
                analysis_survey = Survey.objects.get(pk=request.GET['survey'])

                new_graph_analysis = AnalysisGraph.objects.create(creator=request.user,
                                                                  name=analysis_name,
                                                                  survey=analysis_survey,
                                                                  questions_graphs=terms)
                new_graph_analysis.save()
                redirect_pk = new_graph_analysis.pk

                return redirect('./graph?analysis=' + str(redirect_pk))

            elif request.POST['operation'] == "overwrite":

                analysis_id = request.GET['analysis']
                overwrite_analysis = AnalysisGraph.objects.get(pk=analysis_id)

                overwrite_analysis.questions_graphs = terms
                overwrite_analysis.save()
                redirect_pk = overwrite_analysis.pk

                return redirect('./graph?analysis=' + str(redirect_pk))
