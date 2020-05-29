from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.registration + ' - ' + self.user.username