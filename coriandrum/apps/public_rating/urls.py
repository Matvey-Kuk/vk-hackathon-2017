from django.contrib import admin
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^leaderboard$", views.leaderboard, name="leaderboard"),
    url(r"^contributor/(?P<user_id>[a-zA-Z0-9]+)$", views.contributor, name="contributor"),

]
