from django.shortcuts import redirect
from django.views.generic import CreateView

from ..models.survey import Survey, Question, Choice
from ..models.annotation import Annotation, Classification, Word
from ..forms.surveys import AnnotationWordForm

import random


class Create(CreateView):
    template_name = 'annotation/word_annotation.html'
    model = Word
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        annotation_id = self.kwargs.get('survey_id')

        if Annotation.objects.filter(survey=survey).exists():
            if Annotation.objects.get(pk=annotation_id):
                annotation = Annotation.objects.get(pk=annotation_id)
            else:
                annotation = Annotation.objects.get(pk=1)
        else:
            # TODO: redirect user to create name for annotation
            annotation = Annotation.objects.create(name="Standard annotation", survey=survey)

        classifications = Classification.objects.filter(annotation=annotation.id)
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

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        annotation_id = self.kwargs.get('annotation_id')
        annotation = Annotation.objects.get(pk=annotation_id)

        # make sure we get a unique color
        random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)
        while Classification.objects.filter(annotation=annotation, color=random_hex_color).exists():
            random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)

        # this is where POST data transformations and magic happens

        request.POST._mutable = True
        # Our form is using the model Word
        form.data['text'] = form.data['word_selection']
        form.data['choice'] = Choice.objects.get(pk=form.data['choice_id_selected'])

        # check if the classification existing already
        # if yes    -> store word in it,
        # else      -> create new classification and store word in there
        if Classification.objects.filter(name=form.data['classification'], survey=survey).exists():
            form.data['classification'] = Classification.objects.get(name=form.data['classification'],
                                                                     survey=survey)
        else:
            form.data['classification'] = Classification.objects.create(name=form.data['classification'],
                                                                        survey=survey,
                                                                        color=random_hex_color)

        request.POST._mutable = False

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=True)
        print(self.object)
        return redirect('./annotate')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
