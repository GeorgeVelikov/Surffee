from django.shortcuts import redirect
from django.views.generic import CreateView

from ..models.survey import Survey, Question, Choice
from ..models.annotation import Word
from ..forms.surveys import AnnotationWordForm


class Create(CreateView):
    template_name = 'annotation/word_annotation.html'
    model = Word
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        questions = Question.objects.filter(survey=survey_id)

        choices = Choice.objects.filter(question__in=questions)
        print("GEEEEEEEEEEEEEETTTTTTTTT")
        choice_dict = {}

        for choice in choices:
            choice_dict[choice] = choice.choice_text.split()

        return self.render_to_response(
            self.get_context_data(form=form,
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
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=True)
        return redirect('./')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
