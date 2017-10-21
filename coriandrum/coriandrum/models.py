import json
import requests

from django.db import models
from django.contrib.auth.models import AbstractUser


class CoriandrumUser(AbstractUser):
    vk_user_id = models.IntegerField(unique=True, blank=True, null=True)
    raw_vk_user_cache = models.TextField(blank=True, default="")
    level = models.IntegerField(default=0, unique=False)

    def save(self, *args, **kwargs):
        if self.username == "":
            self.username = "vk_" + str(self.vk_user_id)
        return super(CoriandrumUser, self).save(*args, **kwargs)

    @property
    def achievements(self):
        return Achievement.objects.all()

    @property
    def raw_vk_user(self):
        if self.raw_vk_user_cache == "":
            self.raw_vk_user_cache = json.dumps(requests.get(
                "https://api.vk.com/method/users.get?uids=" + str(self.vk_user_id) + "&fields=photo_200"
            ).json()['response'][0])
            self.save()
        return json.loads(self.raw_vk_user_cache)

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

    STATUS_NEW = 'new'
    STATUS_IN_CONSIDERATION = 'in_consideration'
    STATUS_LOOKS_INTERESTING = 'looks_interesting'
    STATUS_TRASH = 'trash'
    STATUS_PUBLISHED = 'published'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый пост'),
        (STATUS_IN_CONSIDERATION, 'Заблокирован редактором на осознание'),
        (STATUS_LOOKS_INTERESTING, 'Понравился редактору'),
        (STATUS_TRASH, 'В топке'),
        (STATUS_PUBLISHED, 'Опубликован'),
    )

    raw_vk_attachments_payload = models.TextField(default="")

    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    author = models.ForeignKey(CoriandrumUser, on_delete=models.CASCADE)
    text = models.TextField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print(self.raw_vk_attachments_payload)
        super(Post, self).save(force_insert=False, force_update=False,
                               using=None, update_fields=None)


class PostAttachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    raw_vk_attachment_payload = models.TextField()
