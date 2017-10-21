from django.shortcuts import render
from django.http import HttpResponse

from coriandrum.models import CoriandrumUser, Achievement, Post


def leaderboard(request):
    if request.method == "GET":
        return render(request, "public_rating/leaderboard.html")


def contributor(request, user_id):
    if request.method == "GET":
        user = CoriandrumUser.objects.filter(vk_user_id=user_id)[0]
        if not user:
            return HttpResponse("404", status=404)
        context = {
            "user_id": user.vk_user_id,
            "level": user.level,
        }
        return render(request, "public_rating/contributor.html", context)