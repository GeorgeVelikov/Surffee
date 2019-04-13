from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView
from ...models.survey import Survey, Question, Choice
from ...models.annotation import Annotation, Word
from ...forms.annotation import AnnotationWordForm

from ..helper import delete_unused_classifications


class ClassificationCreator(CreateView):
    template_name = 'annotation/word_annotation.html'
    model = Word
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            raise PermissionDenied("You are not logged in")

        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        annotation_id = self.kwargs.get('annotation_id')
        annotation = Annotation.objects.get(pk=annotation_id)

        if request.user.pk != survey.creator.pk:
            raise PermissionDenied("You do not own the survey")

        if request.user.pk != annotation.creator.pk:
            raise PermissionDenied("You do not own the annotation")

        classifications = delete_unused_classifications(annotation)
        words = Word.objects.filter(classification__in=classifications)

        questions = Question.objects.filter(survey=survey_id)
        choices = Choice.objects.filter(question__in=questions)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  annotation=annotation,
                                  classifications=classifications,
                                  words=words,
                                  survey=survey,
                                  choices=choices,
                                  )
        )
