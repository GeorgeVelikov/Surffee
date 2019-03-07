from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from ..models.survey import Survey, Question, Choice
from ..models.annotation import Annotation, Classification, Word
from ..forms.surveys import AnnotationWordForm

import random

from .helper import check_existing_word_dominates_new_word, check_overwrite_existing_word, create_new_classification


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

        choice = Choice.objects.get(pk=form.data['choice_id_selected'])
        word_text = form.data['word_selection']

        word_start = choice.choice_text.find(word_text)
        word_end = word_start + len(word_text)

        # this is where POST data transformations and magic happens
        request.POST._mutable = True
        # Our form is using the model Word
        form.data['text'] = word_text
        form.data['choice'] = choice.pk
        form.data['start'] = word_start
        form.data['end'] = word_end

        # check if the classification existing already
        # if yes    -> store word in it,
        # else      -> create new classification and store word in there
        classification_annotation = Classification.objects.filter(name=form.data['classification_name'],
                                                                  annotation=annotation)
        if classification_annotation.exists():

            sub_words = Word.objects.filter(choice=choice.pk,
                                            classification=classification_annotation.first().pk)

            if sub_words.exists():

                # define sub_word as a word contained in our new selected text for some choice
                # e.g. sub_word -> "ello", selection -> "Hello World"
                for sub_word in sub_words:
                    if sub_word.text in word_text and len(sub_word.text) < len(word_text):
                        sub_word.delete()

            # define dom_word as a word that contains the new selected text for some choice
            # e.g. dom_word -> "Some word", selection -> "SoMe"
            dom_words = Word.objects.filter(choice=choice.pk,
                                            text__icontains=word_text,
                                            classification=classification_annotation.first().pk)
            if dom_words.exists():
                for dom_word in dom_words:
                    if word_text in dom_word.text:
                        return redirect('./' + str(annotation_id))

            form.data['classification'] = Classification.objects.get(name=form.data['classification_name'],
                                                                     annotation=annotation).pk
        else:
            # make sure we get a unique color
            random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)
            while Classification.objects.filter(annotation=annotation, color=random_hex_color).exists():
                random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)

            form.data['classification'] = Classification.objects.create(name=form.data['classification_name'],
                                                                        annotation=annotation,
                                                                        color=random_hex_color).pk

        request.POST._mutable = False

        return self.finish(form, annotation_id)

    def form_valid(self, form, id):
        self.object = form.save(commit=True)
        return redirect('./'+str(id))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def finish(self, form, id):
        if form.is_valid():
            return self.form_valid(form, id)
        else:
            return self.form_invalid(form)


class AddOne(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        classification_name = self.kwargs.get('class')
        word_text = self.kwargs.get('word_text')

        word_start = choice.choice_text.find(word_text)
        word_end = word_start + len(word_text)

        classification_annotation = Classification.objects.filter(name=classification_name,
                                                                  annotation=annotation)
        if classification_annotation.exists():
            check_overwrite_existing_word(choice, classification_annotation, word_text)

            check_existing_word_dominates_new_word(choice, classification_annotation, annotation, word_text, survey.id)

            classification = Classification.objects.get(name=classification_name,
                                                        annotation=annotation).pk

        else:
            classification = create_new_classification(classification_name, annotation)
            classification.save()

        word = Word.objects.create(text=word_text,
                                   start=word_start,
                                   end=word_end,
                                   choice=choice,
                                   classification=classification)
        word.save()

        return redirect('/surveys/'+str(survey.id)+'/annotate/'+str(annotation.id))


class AddAll(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        classification_name = self.kwargs.get('class')
        word_text = self.kwargs.get('word_text')

        all_questions = Question.objects.filter(survey=choice.question.survey)
        all_choices = Choice.objects.filter(question__in=all_questions)
        all_words = Word.objects.filter(choice__in=all_choices)

        classification_annotation = Classification.objects.filter(name=classification_name,
                                                                  annotation=annotation)

        for choice in all_choices:
            if choice.choice_text.find(word_text) == -1:
                continue
            word_start = choice.choice_text.find(word_text)
            word_end = word_start + len(word_text)

            if classification_annotation.exists():
                for word in all_words:
                    if word_text in word.text and len(word.text) < len(word_text):
                        continue

                    if word.text in word_text and word.id:
                        word.delete()

                classification = Classification.objects.get(name=classification_name,
                                                            annotation=annotation)

            else:
                classification = create_new_classification(classification_name, annotation)
                classification.save()

            word = Word.objects.create(text=word_text,
                                       start=word_start,
                                       end=word_end,
                                       choice=choice,
                                       classification=classification)
            word.save()

        return redirect('/surveys/'+str(survey.id)+'/annotate/'+str(annotation.id))


class DeleteOne(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        classification_name = self.kwargs.get('class')
        word_text = self.kwargs.get('word_text')

        word_start = choice.choice_text.find(word_text)
        word_end = word_start + len(word_text)

        return redirect('/surveys/' + str(survey.id) + '/annotate/' + str(annotation.id))


class DeleteAll(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        classification_name = self.kwargs.get('class')
        word_text = self.kwargs.get('word_text')

        word_start = choice.choice_text.find(word_text)
        word_end = word_start + len(word_text)

        return redirect('/surveys/' + str(survey.id) + '/annotate/' + str(annotation.id))
