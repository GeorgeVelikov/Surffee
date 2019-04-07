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
                                  all_user_surveys=list(all_user_surveys),
                                  )
        )
