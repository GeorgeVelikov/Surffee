from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import UpdateView

from ...models.survey import Survey, Question, Choice
from ...models.annotation import Annotation

from ..helper import delete_overlay_word_classifications


class DeleteAll(UpdateView):
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
