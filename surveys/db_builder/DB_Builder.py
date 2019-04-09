from ..models.survey import Survey, Question, Choice
from ..models.user import Researcher

import random
import sys


# responds to the survey with randomised answers
def take_survey(sur_id, no_of_resp):
    survey = Survey.objects.get(id=sur_id)
    say("\nAnswering Survey %s - %d respondents..." % (survey.name, no_of_resp))
    for question in survey.question_set.all():
        choice_set = list(question.choice_set.all())
        set_size = len(choice_set)
        if question.type == 'M':
            for x in range(no_of_resp):
                no_of_choices = random.randrange(1, set_size+1)
                choices = random.sample(range(set_size), no_of_choices)
                for y in choices:
                    choice = choice_set[y]
                    choice.votes += 1
                    choice.save()
        else:
            for x in range(no_of_resp):
                index = random.randrange(set_size)
                choice = choice_set[index]
                choice.votes += 1
                choice.save()
        question_text = question.question_text
        if len(question_text) >= 20:
            question_text = question_text[:15] + '...'
        say("Answered: %s" % question_text[:])


# Survey Creation

def add_choice(text, q_id):
    Choice(
        question=Question.objects.get(id=q_id),
        choice_text=text
    ).save()


def add_question(data, sur_id):
    survey = Survey.objects.get(id=sur_id)
    Question(
        survey=Survey.objects.get(id=sur_id),
        question_text=data[0],
        type=data[1].upper()
    ).save()
    return Question.objects.get(survey=survey, question_text=data[0]).id


def new_survey(data, path):
    active = False
    pi = None

    if data[3] == 'active':
        active = True
    if len(data) == 6 and data[4] != 'none':
        src = open(path + 'pi_choices/' + data[4])
        pi = str([x.strip() for x in src.readlines()])
        src.close()

    r = Researcher.objects.get(username=data[0])
    Survey(
        creator=r,
        name=data[1],
        description=data[2],
        active=active,
        pi_choices=pi
    ).save()
    return Survey.objects.get(creator=r, name=data[1]).id


# User Creation

def superuser(data):
    Researcher.objects.create_superuser(
        username=data[0],
        password=data[1],
        email=data[2]
    ).save()


def user(data):
    Researcher.objects.create_user(
        username=data[0],
        password=data[1],
        email=data[2]
    ).save()


# Check for pre-existing users and surveys

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


# Helper functions

# Sanitise input, allows content files to be more readable
def clean_line(line):
    r = []
    for x in line.strip().split(';'):
        r.append(x.strip())
    return r


# prints given text and flushes the sys.stdout
def say(text):
    sys.stdout.write(str(text) + '\n')
    sys.stdout.flush()


# asks to specify base datasets for DB_Builder (users and surveys)
def get_file(path):
    say("Select the dataset for %s" % path)
    f = sys.stdin.readline().strip()
    if f == '':
        f = 'default'
    return f


class Build:

    def __init__(self):

        self.path = 'surveys/db_builder/'
        self.users = update_users()
        self.report = ''

        say("Pre-existing users: %s" % (', '.join(self.users)))
        self.userset = self.path + 'users/' + get_file('users')
        self.surveyset = self.path + 'surveys/' + get_file('surveys')

        say("Initialising the building process...\n")
        self.register_users()
        self.register_surveys()
        self.summary()

    # username ; password ; email ; [superuser]
    def register_users(self):

        src = open(self.userset)
        for line in src.readlines():
            line = clean_line(line)
            attr_no = len(line)

            if line[0] in self.users:
                say("%s - Failed to create." % line[0])
                self.report += line[0] + ' - user omitted. User with this name already exists.\n'
            elif attr_no == 3:
                user(line)
                self.users.append(line[0])
                say("%s - User Created" % line[0])
            elif attr_no == 4 and line[3] == 'superuser':
                superuser(line)
                self.users.append(line[0])
                say("%s = Superuser Created" % line[0])
            else:
                say("%s - Failed to create." % line[0])
                self.report += line[0] + ' - user omitted. Ill-formatted line.\n'

        src.close()

    # creator ; name ; description ; (in)active ; pi_choices ; question set ; [no. of respondents]
    def register_surveys(self):

        src = open(self.surveyset)
        for line in src.readlines():
            line = clean_line(line)
            users_surveys = [str(x) for x in Researcher.objects.get(username=line[0]).survey_set.all()]

            if len(line) != 6 and len(line) != 7:
                say("\tFailed to create survey %s" % line[1])
                self.report += line[1] + ' - survey omitted. Ill-formatted line.\n'
            elif line[0] not in self.users:
                say("\tFailed to create survey %s" % line[1])
                self.report += line[1] + ' - survey omitted. User ' + line[0] + ' does not exist.\n'
            else:
                if line[1] in users_surveys:
                    # If User already has a survey with this name, append (1), (2),... to name
                    c = 1
                    while True:
                        temp = line[1] + '(' + str(c) + ')'
                        if temp not in users_surveys:
                            line[1] = temp
                            break
                        c += 1
                say("Building Survey: %s" % line[1])
                line[2] = self.get_description(line[2])
                sur_id = new_survey(line, self.path)
                self.register_questions(sur_id, line[5])
                if len(line) == 7:
                    take_survey(sur_id, int(line[6]))
        src.close()

    # question text ; Single/Multi ; choice set
    def register_questions(self, sur_id, question_set):
        src = open(self.path + 'questions/' + question_set)
        sur_questions = []
        for line in src.readlines():
            line = clean_line(line)

            if len(line) != 3:
                say("\tFailed to add question %s" % line[0])
                self.report += line[0] + ' - question omitted. Ill-formatted line.\n'
            elif line[0] in sur_questions:
                say("\tFailed to add question %s" % line[0])
                self.report += line[0] + ' - question omitted. Duplicate question.\n'
            else:
                say("\tAdding Question: %s" % line[0])
                sur_questions.append(line[0])
                q_id = add_question(line, sur_id)
                self.register_choices(q_id, line[2])
        src.close()

    # each line is separate choice
    def register_choices(self, question, choice_set):
        src = open(self.path + 'choices/' + choice_set)
        choices = list(set([c.strip() for c in src.readlines()]))   # remove duplicate choices
        for choice in choices:
            say("\t\tAdding Choice: %s" % choice)
            add_choice(choice, question)
        src.close()

    # the whole file is the description
    def get_description(self, source):
        src = open(self.path + 'descriptions/' + source)
        desc = src.read().strip()
        src.close()
        return desc

    def summary(self):

        summ = "\nBuilder has finished the process.\n"

        for u in self.users:
            summ += ">>>\t%s\n" % u
            for s in Researcher.objects.get(username=u).survey_set.all():
                summ += "\n\t %s\n" % str(s)
                for q in s.question_set.all():
                    summ += "\t  %s\n" % str(q)
                    for c in q.choice_set.all():
                        summ += "\t\t%s\n" % str(c)

        if self.report != '':
            summ += '\n' + self.report

        say(summ)
