from django.contrib.auth.models import AbstractUser


class Researcher(AbstractUser):
    def __str__(self):
        return self.username
