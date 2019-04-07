# from .models.survey import Survey
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


class Build:

    def __init__(self):
        self.src = open('surveys/builder.txt')
        self.users = {}

        user_no, survey_no = map(int, self.src.readline().strip().split(' '))

        self.update_users()
        self.register_users(user_no)
        self.summary()

    def update_users(self):
        for each in Researcher.objects.all():
            self.users[each.username] = user

    def register_users(self, n):
        for x in range(n):
            line = self.src.readline().strip().split(';')
            attr_no = len(line)

            if line[0] in self.users:
                sys.stdout.write(line[0] + ' already exists, line ' + str(x+1) + ' omitted\n')
            elif attr_no == 3:
                self.users[line[0]] = user(line[0], line[1], line[2])
            elif attr_no == 4 and line[3] == 'superuser':
                self.users[line[0]] = superuser(line[0], line[1], line[2])
            else:
                sys.stdout.write(
                    'Omitting ill-formatted line for user ' + line[0] + '. Line ' + str(x+1) + '\n')
            sys.stdout.flush()

    def summary(self):
        summ = "\nBuilder has finished the process.\n"
        summ += "\tUsers:\n"
        for name in self.users:
            summ += "\t\t" + name + "\n"
        sys.stdout.write(summ + "\n")
        sys.stdout.flush()
