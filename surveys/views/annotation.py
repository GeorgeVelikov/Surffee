from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from ..models.survey import Survey, Question, Choice
from ..models.annotation import Annotation, Classification, Word
from ..forms.surveys import AnnotationWordForm

from .helper import check_existing_word_dominates_new_word, check_overwrite_existing_word, create_new_classification, \
    delete_overlay_word_classifications, delete_unused_classifications


class AnnotationManager(CreateView):
    template_name = 'annotation/annotation_manager.html'
    model = Annotation
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        self.object = None
        all_user_annotations = Annotation.objects.filter(creator=request.user)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  all_annotations=all_user_annotations,
                                  )
        )


    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        request.POST._mutable = True
        form.data['creator'] = request.user.pk
        request.POST._mutable = False
        print(form.data)


        return self.finish(form)

    def form_valid(self, form):
        self.object = form.save(commit=True)
        print(self.object)
        print("WWWWWWWWWWWWWWWWWW")
        return redirect('./')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    def finish(self, form):
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AnnotationSelector(CreateView):
    template_name = 'annotation/annotation_selector.html'
    model = Annotation
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)

        all_survey_annotations = Annotation.objects.filter(creator=request.user)

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return self.render_to_response(
            self.get_context_data(form=form,
                                  survey=survey,
                                  all_annotations=all_survey_annotations,
                                  )
        )


class ClassificationCreator(CreateView):
    template_name = 'annotation/word_annotation.html'
    model = Word
    form_class = AnnotationWordForm

    def get(self, request, *args, **kwargs):
        self.object = None
        survey_id = self.kwargs.get('survey_id')
        survey = Survey.objects.get(pk=survey_id)
        annotation_id = self.kwargs.get('annotation_id')

        annotation = Annotation.objects.get(pk=annotation_id)

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


class AddOne(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        classification_name = self.kwargs.get('class')
        word_text = self.kwargs.get('word_text')
        leftover_word = choice.choice_text

        word_count_track = 0

        while leftover_word.find(word_text) >= 0:
            word_start = leftover_word.find(word_text) + word_count_track
            word_end = word_start + len(word_text)

            classification_annotation = Classification.objects.filter(name=classification_name,
                                                                      annotation=annotation)
            if classification_annotation.exists():
                check_overwrite_existing_word(choice, classification_annotation, word_text)

                check_existing_word_dominates_new_word(choice, classification_annotation, annotation, word_text, survey.id)

                classification = Classification.objects.get(name=classification_name,
                                                            annotation=annotation)

            else:
                classification = create_new_classification(classification_name, annotation)
                classification.save()

            delete_overlay_word_classifications(choice, word_start, word_end)

            word = Word.objects.create(text=word_text,
                                       start=word_start,
                                       end=word_end,
                                       choice=choice,
                                       classification=classification)

            leftover_word = choice.choice_text[word_end::]
            word_count_track += (word_end - word_count_track)
            word.save()

        return redirect('/surveys/'+str(survey.id)+'/annotate/'+str(annotation.id))


class AddAll(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        classification_name = self.kwargs.get('class')
        word_to_annotate = self.kwargs.get('word_text')

        all_questions = Question.objects.filter(survey=choice.question.survey)
        all_choices = Choice.objects.filter(question__in=all_questions)

        classification_annotation = Classification.objects.filter(name=classification_name,
                                                                  annotation=annotation)

        for choice in all_choices:
            word_text = choice.choice_text
            word_count_track = 0
            while word_text.find(word_to_annotate) >= 0:
                word_start = word_text.find(word_to_annotate) + word_count_track
                word_end = word_start + len(word_to_annotate)

                if classification_annotation.exists():
                    check_overwrite_existing_word(choice, classification_annotation, word_to_annotate)
                    check_existing_word_dominates_new_word(choice, classification_annotation, annotation,
                                                           word_to_annotate, survey.id)

                    classification = Classification.objects.get(name=classification_name,
                                                                annotation=annotation)

                else:
                    classification = create_new_classification(classification_name, annotation)
                    classification.save()

                delete_overlay_word_classifications(choice, word_start, word_end)

                word = Word.objects.create(text=word_to_annotate,
                                           start=word_start,
                                           end=word_end,
                                           choice=choice,
                                           classification=classification)
                word.save()

                word_text = choice.choice_text[word_end::]
                word_count_track += (word_end-word_count_track)

        return redirect('/surveys/'+str(survey.id)+'/annotate/'+str(annotation.id))


class DeleteOne(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        word_text = self.kwargs.get('word_text')
        leftover_word = choice.choice_text
        word_count_track = 0

        while leftover_word.find(word_text) >= 0:
            word_start = leftover_word.find(word_text) + word_count_track
            word_end = word_start + len(word_text)

            delete_overlay_word_classifications(choice, word_start, word_end)
            leftover_word = choice.choice_text[word_end::]
            word_count_track += (word_end - word_count_track)

        return redirect('/surveys/' + str(survey.id) + '/annotate/' + str(annotation.id))


class DeleteAll(UpdateView):
    def get(self, request, *args, **kwargs):
        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        word_text = self.kwargs.get('word_text')

        word_start = choice.choice_text.find(word_text)
        word_end = word_start + len(word_text)

        all_questions = Question.objects.filter(survey=choice.question.survey)
        all_choices = Choice.objects.filter(question__in=all_questions)

        for ch in all_choices:
            leftover_word = ch.choice_text
            word_count_track = 0

            while leftover_word.find(word_text) >= 0:
                word_start = leftover_word.find(word_text) + word_count_track
                word_end = word_start + len(word_text)

                delete_overlay_word_classifications(ch, word_start, word_end)
                leftover_word = ch.choice_text[word_end::]
                word_count_track += (word_end - word_count_track)

        return redirect('/surveys/' + str(survey.id) + '/annotate/' + str(annotation.id))
