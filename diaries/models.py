from django.db import models
from django.contrib.auth.models import User


class Diary(models.Model):
    KIND_CHOICES = [
        ('private', 'private'),
        ('public', 'public')
    ]
    title = models.CharField(max_length=200)
    expiration = models.DateTimeField(null=True)
    kind = models.CharField(choices=KIND_CHOICES, default='private', max_length=7)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Дневник {self.title}'


class Note(models.Model):
    text = models.TextField()

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)

    def __str__(self):
        return f'Страница дневника {self.diary.title}'



