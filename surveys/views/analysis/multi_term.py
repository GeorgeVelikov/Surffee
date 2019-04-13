from django.views.generic import CreateView

from surveys.models.annotation import Annotation
from surveys.models.survey import Survey
from surveys.forms.analysis import AnalysisCreator

from ...views.error import permission_user_logged_in


class AnalysisMultipleTerm(CreateView):
    template_name = 'analysis/multiple.html'
    model = Annotation
    form_class = AnalysisCreator

    def get(self, request, *args, **kwargs):
        permission_user_logged_in(request)

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        all_surveys = Survey.objects.filter(creator=request.user).values('pk', 'name')

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_surveys=all_surveys,
                                  )
        )
