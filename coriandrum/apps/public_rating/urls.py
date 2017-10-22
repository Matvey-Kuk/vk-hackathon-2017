from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^leaderboard$", views.leaderboard, name="leaderboard"),
    url(r"^entry$", views.entry, name="entry"),
    url(r"^contributor/(?P<user_id>[a-zA-Z0-9]+)(?P<is_admin>/admin)?$", views.contributor, name="contributor"),
]
