from .models.survey import Survey, Question, Choice
from .models.user import Researcher

import sys


def add_question(data, survey):
    Question(
        survey=Survey.objects.get(name=survey),
        question_text=data[0],
        type=data[1].upper()
    ).save()


def new_survey(data, path):
    active = False
    pi = None

    if data[3] == 'active':
        active = True
    if len(data) == 6 and data[5] != 'none':
        src = open(path + 'pi_choices/' + data[5])
        pi = str([x.strip() for x in src.readlines()])
        src.close()

    Survey(
        creator=Researcher.objects.get(username=data[0]),
        name=data[1],
        description=data[2],
        active=active,
        pi_choices=pi
    ).save()


def superuser(data):
    Researcher.objects.create_superuser(
        username=data[0],
        password=data[1],
        email=data[2]
    ).save()
    return data[0]


def user(data):
    Researcher.objects.create_user(
        username=data[0],
        password=data[1],
        email=data[2]
    ).save()
    return data[0]


def update_users():
    users = []
    for each in Researcher.objects.all():
        users.append(str(each))
    return users


def update_surveys():
    surveys = {}
    for each in Survey.objects.all():
        surveys[each.name] = [str(x) for x in each.question_set.all()]
    return surveys


class Build:

    def __init__(self):

        self.path = 'surveys/db_builder/'
        self.users = update_users()
        self.surveys = update_surveys()
        self.report = ''

        self.register_users()
        self.register_surveys()
        self.summary()

    # username ; password ; email ; [superuser]
    def register_users(self):

        src = open(self.path + 'users')
        for line in src.readlines():
            line = line.strip().split(';')
            attr_no = len(line)

            if line[0] in self.users:
                self.report += line[0] + ' - user omitted. User with this name already exists.\n'
            elif attr_no == 3:
                self.users.append(user(line))
            elif attr_no == 4 and line[3] == 'superuser':
                self.users.append(superuser(line))
            else:
                self.report += line[0] + ' - user omitted. Ill-formatted line.\n'

        src.close()

    # creator ; name ; description ; (in)active ; no. of questions ; pi_choices ; question set
    def register_surveys(self):

        src = open(self.path + 'surveys')
        for line in src.readlines():
            line = line.strip().split(';')

            if len(line) != 7:
                self.report += line[1] + ' - survey omitted. Ill-formatted line.\n'
                break
            elif line[1] in self.surveys:
                self.report += line[1] + ' - survey omitted. Survey with this name already exists.\n'
                break
            elif line[0] not in self.users:
                self.report += line[1] + ' - survey omitted. User ' + line[0] + ' does not exist.\n'
                break
            new_survey(line, self.path)
            self.register_questions(line[1], line[6])
        src.close()

    # question text ; Single/Multi ; choice set
    def register_questions(self, sur_name, question_set):
        survey = Survey.objects.get(name=sur_name)
        src = open(self.path + 'questions/' + question_set)
        self.surveys[sur_name] = []
        for line in src.readlines():
            line = line.strip().split(';')
            if len(line) != 3:
                self.report += line[0] + ' - question omitted for survey ' + sur_name + '. Ill-formatted line.\n'
            add_question(line, survey)
            self.surveys[sur_name].append(line[0])
        src.close()

    def summary(self):

        summ = "\nBuilder has finished the process.\n"
        summ += "\tUsers:\n"

        for name in self.users:
            summ += "\t\t" + name + "\n"

        summ += "\tSurveys:\n"
        for name in self.surveys:
            summ += "\t\t" + name + "\n"
            for question in self.surveys[name]:
                summ += "\t\t\t" + question + "\n"

        if self.report != '':
            summ += '\n' + self.report

        sys.stdout.write(summ + "\n")
        sys.stdout.flush()
