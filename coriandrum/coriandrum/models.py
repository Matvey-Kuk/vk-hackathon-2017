# -*- coding: utf-8 -*-

import json
import requests

from django.db import models
from django.contrib.auth.models import AbstractUser


class CoriandrumUser(AbstractUser):
    vk_user_id = models.IntegerField(unique=True, blank=True, null=True)
    raw_vk_user_cache = models.TextField(blank=True, default="")

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
        user_data = self.raw_vk_user
        if "first_name" in user_data and "last_name" in user_data:
            return user_data['first_name'] + " " + user_data['last_name']
        else:
            return None

    @property
    def vk_avatar(self):
        user_data = self.raw_vk_user
        if "photo_200" in user_data:
            return user_data['photo_200']
        else:
            return None

    @property
    def all_posts(self):
        ''' Return all posts by a user '''
        if self.vk_user_id:
            user_posts = Post.objects.filter(author__vk_user_id__contains=
                                             self.vk_user_id)
            return user_posts
        else:
            return []

    @property
    def n_all_posts(self):
        return len(self.all_posts)

    @property
    def published_posts(self):
        published_posts = ([p for p in self.all_posts
                            if p.status == "published"])
        return published_posts

    @property
    def n_published(self):
        return len(self.published_posts)

    @property
    def level(self):
        n_published = len(self.published_posts)
        reqs = {
            0: 0,
            1: 1,
            2: 2,
            3: 5,
            4: 10,
            5: 20,
            6: 30,
        }
        for level in range(7)[::-1]:
            if n_published >= reqs[level]:
                return level

    @property
    def recently_leveled_up(self):
        '''
        Return True if the last published post resulted in a
        levelup of the user '''
        # TODO: remove duplication
        if self.n_published in [1, 2, 5, 10, 20, 30]:
            return True
        else:
            return False


class Achievement(models.Model):
    name = models.TextField()
    image = models.ImageField()


class Post(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_CONSIDERATION = 'in_consideration'
    STATUS_LOOKS_INTERESTING = 'looks_interesting'
    STATUS_TRASH = 'trash'
    STATUS_PUBLISHED = 'published'
    STATUS_INVALID = 'invalid'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый пост'),
        (STATUS_IN_CONSIDERATION, 'Заблокирован редактором на осознание'),
        (STATUS_LOOKS_INTERESTING, 'Понравился редактору'),
        (STATUS_TRASH, 'В топке'),
        (STATUS_PUBLISHED, 'Опубликован'),
        (STATUS_INVALID, 'Не валиден'),
    )

    raw_vk_attachments_payload = models.TextField(default="", null=True, blank=True)

    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )

    in_consideration_by_moderator = models.ForeignKey(
        CoriandrumUser, on_delete=models.CASCADE, null=True, blank=True,
        related_name="is_considered_by"
    )

    author = models.ForeignKey(CoriandrumUser, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        payload = {}
        if self.pk is None:
            payload = {
                "type": "new_post",
                "vk_user_id": self.author.vk_user_id
            }
        else:
            old_model = Post.objects.get(pk=self.pk)
            print(old_model.status)
            print(self.status)
            payload = {
                "type": "new_post",
                "vk_user_id": self.author.vk_user_id
            }

        print(requests.post(
            "https://coriandrum-chatbot.herokuapp.com/update",
            data=json.dumps(payload),
            headers={'content-type': 'application/json'}
        ).text)

        super(Post, self).save(force_insert=False, force_update=False,
                               using=None, update_fields=None)


class PostAttachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    raw_vk_attachment_payload = models.TextField()
