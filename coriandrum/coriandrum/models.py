from django.db import models
from django.contrib.auth.models import AbstractUser


class CoriandrumUser(AbstractUser):
    vk_user_id = models.IntegerField(unique=True, blank=True, null=True)

    @property
    def achievements(self):
        return Achievement.objects.all()


class Achievement(models.Model):
    name = models.TextField()
    image = models.ImageField()


class Post(models.Model):
    author = models.ForeignKey(CoriandrumUser, on_delete=models.CASCADE)
    text = models.TextField()
