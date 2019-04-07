from .models.survey import Survey
from .models.user import Researcher

import sys


def superuser(username, password, email):
    r = Researcher.objects.create_superuser(
        username=username,
        password=password,
        email=email
    ).save()
    return r


def user(username, password, email):
    r = Researcher.objects.create_user(
        username=username,
        password=password,
        email=email
    ).save()
    return r


def update_users():
    users = {}
    for each in Researcher.objects.all():
        users[each.username] = each
    return users


def update_surveys():
    surveys = {}
    for each in Survey.objects.all():
        surveys[each.name] = each
    return surveys


class Build:

    def __init__(self):

        self.users = update_users()
        self.surveys = update_surveys()

        self.register_users()
        self.summary()

    def register_users(self):

        src = open('surveys/db_builder/users.txt')
        for line in src.readlines():
            line = line.strip().split(';')
            attr_no = len(line)

            if line[0] in self.users:
                sys.stdout.write(line[0] + ' already exists, ' + 'omitted\n')
                sys.stdout.flush()
            elif attr_no == 3:
                self.users[line[0]] = user(line[0], line[1], line[2])
            elif attr_no == 4 and line[3] == 'superuser':
                self.users[line[0]] = superuser(line[0], line[1], line[2])
            else:
                sys.stdout.write('Omitting ill-formatted line for user ' + line[0] + '.\n')
                sys.stdout.flush()

        src.close()

    def summary(self):

        summ = "\nBuilder has finished the process.\n"
        summ += "\tUsers:\n"

        for name in self.users:
            summ += "\t\t" + name + "\n"

        summ += "\tSurveys:\n"
        for name in self.surveys:
            summ += "\t\t" + name + "\n"

        sys.stdout.write(summ + "\n")
        sys.stdout.flush()
