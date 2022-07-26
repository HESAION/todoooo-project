from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Это значит что поле не обязательно к заполнению
    created = models.DateTimeField(auto_now_add=True)
    datecomplited = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # эта модель позволит связать конкретную

                                                              # запись с конкретным пользователем

    def __str__(self):
        return self.title
