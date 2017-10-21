import os
import sys
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'coriandrum.settings'
django.setup()

from coriandrum.models import CoriandrumUser, Post

import random



def create_published_post(user):
    p = Post.objects.create(text="post text", author=user, status="published")
    p.save()


def create_users_with_posts(n_users):
    start_id = 200
    for vk_user_id in range(start_id, start_id+n_users):
        u = CoriandrumUser.objects.create(vk_user_id = vk_user_id)
        u.save()
        n_posts = 0
        if random.choice([0,1]):
            n_posts = random.choice(range(35))
            for p in range(n_posts):
                create_published_post(u)
        print "Created user {} with {} published posts".format(vk_user_id,
                                                               n_posts)


if __name__ == '__main__':
    usage = ("Usage: python create_users.py n_users\n"
             "Creates n_users users with random number of published posts")
    if len(sys.argv) == 1:
        print usage
        exit()
    n_users = int(sys.argv[1])
    create_users_with_posts(n_users)