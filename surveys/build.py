from .models.survey import Survey
from .models.user import Researcher

import sys
import time


# TODO: add pi_choices
def new_survey(data, path):
    active = False
    pi = None

    if data[3] == 'active':
        active = True
    if len(data) == 6:
        src = open(path + 'pi_choices/' + data[5] + '.txt')
        pi = str([x.strip() for x in src.readlines()])
        src.close()

    s = Survey(
        creator=Researcher.objects.get(username=data[0]),
        name=data[1],
        description=data[2],
        active=active,
        pi_choices=pi
    ).save()
    return s


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
        surveys[each.name] = each
    return surveys


class Build:

    def __init__(self):

        self.path = 'surveys/db_builder/'
        self.users = update_users()
        self.surveys = update_surveys()
        self.report = ''

        self.register_users()
        time.sleep(0.5)
        self.register_surveys()
        self.summary()

    # username ; password ; email ; [superuser]
    def register_users(self):

        src = open(self.path + 'users.txt')
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

    # creator ; name ; description ; (in)active ; no. of questions ; pi_choices
    def register_surveys(self):

        src = open(self.path + 'surveys.txt')
        for line in src.readlines():
            line = line.strip().split(';')

            if (len(line) < 5) or (len(line) > 6):
                self.report += line[1] + ' - survey omitted. Ill-formatted line.\n'
                break
            elif line[1] in self.surveys:
                self.report += line[1] + ' - survey omitted. Survey with this name already exists.\n'
                break
            elif line[0] not in self.users:
                self.report += line[1] + ' - survey omitted. User ' + line[0] + ' does not exist.\n'
                break

            self.surveys[line[1]] = new_survey(line, self.path)


        src.close()

    def summary(self):

        summ = "\nBuilder has finished the process.\n"
        summ += "\tUsers:\n"

        for name in self.users:
            summ += "\t\t" + name + "\n"

        summ += "\tSurveys:\n"
        for name in self.surveys:
            summ += "\t\t" + name + "\n"

        if self.report != '':
            summ += '\n' + self.report

        sys.stdout.write(summ + "\n")
        sys.stdout.flush()
