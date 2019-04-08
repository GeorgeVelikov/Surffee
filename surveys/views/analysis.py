from django.shortcuts import redirect
from django.views.generic import CreateView

from surveys.models.annotation import Annotation
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

        print(form.data)

        analysis_type = form.data['analysis_option']

        if analysis_type == "single":
            return redirect('/surveys/analysis/single')
        elif analysis_type == "multiple":
            return redirect('/surveys/analysis/multiple')
        elif analysis_type == "graph":
            return redirect('/surveys/analysis/graph')

        return redirect('/surveys/analysis')


class AnalysisSingleTerm(CreateView):
    template_name = 'analysis/single.html'
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
