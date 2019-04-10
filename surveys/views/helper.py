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
    random_hex_color = random.randint(0x000000, 0xFFFFFF)
    # make sure we get a unique color
    while 0x505050 < random_hex_color < 0xAEAEAE or not random_hex_color:
        random_hex_color = random.randint(0x000000, 0xFFFFFF)

    while Classification.objects.filter(annotation=annotation, color=("#%06x" % random_hex_color)).exists():
        while 0x505050 < random_hex_color < 0xAEAEAE or not random_hex_color:
            random_hex_color = random.randint(0x000000, 0xFFFFFF)

    instance = Classification.objects.create(name=classification_name,
                                             annotation=annotation,
                                             color=("#%06x" % random_hex_color)
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


def delete_overlay_word_classifications(choice, annotation_start, annotation_end):
    delete_sub_words = Word.objects.filter(choice=choice, start__lte=annotation_start, end__gte=annotation_end) | \
                       Word.objects.filter(choice=choice, start__lt=annotation_end, end__gt=annotation_start)

    for del_word in delete_sub_words:
        del_word.delete()


def delete_unused_classifications(annotation):
    set_of_used_classifications = set()
    all_classifications_annotation = Classification.objects.filter(annotation=annotation.id)
    all_words_classifications = Word.objects.filter(classification__in=all_classifications_annotation)

    for word in all_words_classifications:
        set_of_used_classifications.add(word.classification.name)

    for classif in all_classifications_annotation:
        if classif.name not in set_of_used_classifications:
            classif.delete()
            all_classifications_annotation = all_classifications_annotation.exclude(name=classif.name)

    # this gives a cleansed queryset
    return all_classifications_annotation


def get_age_ranges(pi_set):
    newages = set()
    if 'Age' in pi_set:
        for num in pi_set['Age']:
            for i in range(19, 100, 10):
                low = 9
                if i == 19:
                    low = 1

                if num in range(i - low, i+1):
                    rng = str(i - low) + "-" + str(i)
                    newages.add(rng)

                if num >= 100:
                    newages.add("100+")

        pi_set['Age'] = sorted(newages)
    return pi_set
