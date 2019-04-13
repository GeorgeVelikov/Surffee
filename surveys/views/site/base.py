from ...models.survey import Survey
from ...models.analysis import AnalysisSingle, AnalysisGraph


def base(request):
    username = "Profile"
    surveys_active = []
    surveys_inactive = []

    all_analysis_single = []
    all_analysis_multi = []
    all_analysis_graph = []

    if request.user.is_authenticated:
        username = request.user.username
        all_surveys = Survey.objects.filter(creator=request.user.pk)
        all_analysis_single = AnalysisSingle.objects.filter(creator=request.user.pk)
        all_analysis_multi = []
        all_analysis_graph = AnalysisGraph.objects.filter(creator=request.user.pk)

        for survey in all_surveys:
            if survey.active:
                surveys_active.append(survey)
            else:
                surveys_inactive.append(survey)

    else:
        surveys_active = []
        surveys_inactive = []

    context = {'username': username,
               'surveys_active': surveys_active,
               'surveys_inactive': surveys_inactive,
               'all_analysis_single': all_analysis_single,
               'all_analysis_multi': all_analysis_multi,
               'all_analysis_graph': all_analysis_graph,
               }

    return context
