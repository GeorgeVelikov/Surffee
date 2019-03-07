from ..models.survey import Question
from ..models.annotation import Classification, Word
from django.shortcuts import redirect

import random


def get_ip(request):
    # grab ip address of person
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def get_next_question(answer_instance, question):
    survey_all_questions = Question.objects.filter(survey=question.survey)
    nextq = None
    for sq in survey_all_questions:
        if sq not in answer_instance.question.all():
            nextq = sq
            break
    if nextq:
        return nextq


def create_new_classification(classification_name, annotation):
    # make sure we get a unique color
    random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)
    while Classification.objects.filter(annotation=annotation, color=random_hex_color).exists():
        random_hex_color = "#%06x" % random.randint(0, 0xFFFFFF)

    instance = Classification.objects.create(name=classification_name,
                                             annotation=annotation,
                                             color=random_hex_color
                                             )
    return instance


def check_overwrite_existing_word(choice, classification, word_text):
    sub_words = Word.objects.filter(choice=choice.pk,
                                    classification=classification.first().pk)

    if sub_words.exists():

        # define sub_word as a word contained in our new selected text for some choice
        # e.g. sub_word -> "ello", selection -> "Hello World"
        for sub_word in sub_words:
            if sub_word.text in word_text and len(sub_word.text) < len(word_text):
                sub_word.delete()


def check_existing_word_dominates_new_word(choice, classification, annotation, word_text, survey_id):
    # define dom_word as a word that contains the new selected text for some choice
    # e.g. dom_word -> "Some word", selection -> "SoMe"
    dom_words = Word.objects.filter(choice=choice.pk,
                                    text__icontains=word_text,
                                    classification=classification.first().pk)
    if dom_words.exists():
        for dom_word in dom_words:
            if word_text in dom_word.text:
                return redirect('/surveys/' + str(survey_id) + '/annotate/' + str(annotation.id))

