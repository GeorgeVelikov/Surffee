from ..models import Question


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
