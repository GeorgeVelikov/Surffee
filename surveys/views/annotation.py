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

        if Annotation.objects.filter(survey=survey).exists():
            current_annotation = Annotation.objects.filter(survey=survey).first()
        else:
            # TODO: redirect user to create name for annotation
            current_annotation = Annotation.objects.create(name="Standard annotation", survey=survey)

        classifications = Classification.objects.filter(annotation=current_annotation.id)
        words = Word.objects.filter(classification__in=classifications)

        questions = Question.objects.filter(survey=survey_id)
        choices = Choice.objects.filter(question__in=questions)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  current_annotation=current_annotation,
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

        random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)

        request.POST._mutable = True

        form.data['text'] = form.data['word_selection']

        if Word.objects.filter(classification=form.data['classification']).exists():
            form.data['color'] = Word.objects.filter(classification=form.data['classification']).first().color
        else:
            form.data['color'] = random_hex_color

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
