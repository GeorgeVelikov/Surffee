from django.shortcuts import redirect
from django.views.generic import CreateView

from surveys.models.annotation import Annotation, Classification, Word
from surveys.models.survey import Survey
from surveys.forms.analysis import AnalysisCreator


class Create(CreateView):
    template_name = 'analysis/create_analysis.html'
    model = Annotation
    form_class = AnalysisCreator
    
    def get(self, request, *args, **kwargs):
        self.object = None
        all_user_surveys = Survey.objects.filter(creator=request.user).values('pk', 'name')

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_user_surveys=all_user_surveys,
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        analysis_type = form.data['analysis_option']
        analysis_name = form.data['analysis_name']
        analysis_survey = form.data['survey_to_analyse']

        if analysis_type == "single":
            return redirect('/surveys/analysis/single?name=' + analysis_name + '&survey=' + analysis_survey)
        elif analysis_type == "multiple":
            return redirect('/surveys/analysis/multiple')
        elif analysis_type == "graph":
            return redirect('/surveys/analysis/graph')

        # this is in case something goes wrong, just returns back to the same page
        return redirect('/surveys/analysis')


class AnalysisSingleTerm(CreateView):
    template_name = 'analysis/single.html'
    model = Annotation
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        get_variables = request.GET

        # the two vars we get from the post
        survey_id = int(get_variables['survey'])
        analysis_name = get_variables['name']

        all_annotations = Annotation.objects.filter(creator=request.user)
        classificiations = Classification.objects.filter(annotation__in=all_annotations)
        words = Word.objects.filter(classification__in=classificiations)

        used_annotations = Annotation.objects.none()
        for word in words:
            if word.choice.question.survey.pk == survey_id:
                used_annotations |= Annotation.objects.filter(pk=word.classification.annotation.pk)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  used_annotations=used_annotations,
                                  )
        )


class AnalysisMultipleTerm(CreateView):
    template_name = 'analysis/multi.html'
    model = Annotation
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        all_surveys = Survey.objects.filter(creator=request.user).values('pk', 'name')

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_surveys=all_surveys,
                                  )
        )
