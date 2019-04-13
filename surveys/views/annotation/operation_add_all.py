from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey, Question, Choice
from ...models.annotation import Annotation, Classification, Word

from ..helper import check_existing_word_dominates_new_word, check_overwrite_existing_word, create_new_classification, \
    delete_overlay_word_classifications


class AddAll(UpdateView):
    def get(self, request, *args, **kwargs):
        if not request.user.pk:
            raise PermissionDenied("You are not logged in")

        self.object = None
        survey = Survey.objects.get(pk=self.kwargs.get('survey_id'))
        annotation = Annotation.objects.get(pk=self.kwargs.get('annotation_id'))
        choice = Choice.objects.get(pk=self.kwargs.get('choice_id'))

        if request.user.pk != survey.creator.pk:
            raise PermissionDenied("You do not own the survey")

        if request.user.pk != annotation.creator.pk:
            raise PermissionDenied("You do not own the annotation")

        if request.user.pk != choice.question.survey.creator.pk:
            raise PermissionDenied("You do not own the choice")

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
