from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import CreateView

from ...models.survey import Survey
from ...models.annotation import Annotation, Classification
from ...forms.annotation import AnnotationWordForm


class AnnotationSelector(CreateView):
    template_name = 'annotation/annotation_selector.html'
    model = Annotation
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            raise PermissionDenied("You are not logged in")

        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        if request.user.pk != survey.creator.pk:
            raise PermissionDenied("You do not own the survey")

        all_user_annotations = Annotation.objects.filter(creator=request.user)
        all_classifications = Classification.objects.filter(annotation__in=all_user_annotations)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  survey=survey,
                                  all_annotations=all_user_annotations,
                                  all_classifications_js=list(all_classifications.values()),
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        survey_id = self.kwargs.get('survey_id')
        annotation_id = form.data['select']

        return redirect('/surveys/'+str(survey_id)+'/annotate/'+str(annotation_id))
