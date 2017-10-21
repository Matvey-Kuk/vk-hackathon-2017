import requests

from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import AbstractUser


class CoriandrumUser(AbstractUser):
    vk_user_id = models.IntegerField(unique=True, blank=True, null=True)
    level = models.IntegerField()

    @property
    def achievements(self):
        return Achievement.objects.all()

    @cached_property
    def raw_vk_user(self):
        return requests.get("https://api.vk.com/method/users.get?uids=" + str(self.vk_user_id) + "&fields=photo_200").json()['response'][0]

    @property
    def vk_name(self):
        return self.raw_vk_user['first_name'] + " " + self.raw_vk_user['last_name']

    @property
    def vk_avatar(self):
        return self.raw_vk_user['photo_200']


class Achievement(models.Model):
    name = models.TextField()
    image = models.ImageField()


class Post(models.Model):
    author = models.ForeignKey(CoriandrumUser, on_delete=models.CASCADE)
    text = models.TextField()
