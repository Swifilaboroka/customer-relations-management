from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email
