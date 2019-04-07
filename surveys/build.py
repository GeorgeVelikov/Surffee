# from .models.survey import Survey
from .models.user import Researcher

import sys


def superuser(username, password, email):
    Researcher.objects.create_superuser(
        username=username,
        password=password,
        email=email
    ).save()


def user(username, password, email):
    Researcher.objects.create_user(
        username=username,
        password=password,
        email=email
    ).save()


class Build:

    def __init__(self):
        self.src = open('surveys/builder.txt')
        self.register_users()

    def register_users(self):
        user_no = int(self.src.readline().strip())
        for x in range(user_no):
            line = self.src.readline().strip().split(';')

            attr_no = len(line)
            if line[0] in [str(x) for x in Researcher.objects.all()]:
                sys.stdout.write(line[0] + " already exists, omitted\n")
            elif attr_no == 3:
                user(line[0], line[1], line[2])
            elif attr_no == 4 and line[3] == 'superuser':
                superuser(line[0], line[1], line[2])
            else:
                sys.stdout.write(
                    "Omitting ill-formatted line for user " + line[0] + '\n')


