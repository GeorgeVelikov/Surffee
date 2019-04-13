from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import CreateView

from ...models.annotation import Annotation, Classification
from ...models.annotation import Word
from ...forms.annotation import AnnotationWordForm


class AnnotationManager(CreateView):
    template_name = 'annotation/annotation_manager.html'
    model = Annotation
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            raise PermissionDenied("You are not logged in")

        self.object = None
        all_user_annotations = Annotation.objects.filter(creator=request.user)
        all_classifications = Classification.objects.filter(annotation__in=all_user_annotations)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_annotations=all_user_annotations,
                                  all_annotations_js=list(all_user_annotations.values()),
                                  all_classifications_js=list(all_classifications.values()),
                                  )
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if "create" in form.data:
            request.POST._mutable = True
            form.data['creator'] = request.user.pk
            request.POST._mutable = False
        if "delete" in form.data:
            annot_id = form.data["delete"]
            annot_to_del = Annotation.objects.get(pk=annot_id)
            all_classif_to_del = Classification.objects.filter(annotation=annot_to_del)
            all_words_to_del = Word.objects.filter(classification__in=all_classif_to_del)

            annot_to_del.delete()
            all_classif_to_del.delete()
            all_words_to_del.delete()
            return redirect('/surveys/annotation_manager')

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=True)
        return redirect('./annotation_manager')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))