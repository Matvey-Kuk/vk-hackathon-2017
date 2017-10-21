from django.shortcuts import render
from django.http import HttpResponse

from coriandrum.models import CoriandrumUser, Achievement, Post


def leaderboard(request):
    if request.method == "GET":
        all_users = list(CoriandrumUser.objects.all())
        all_users.sort(key=lambda u: len(u.published_posts), reverse=True)
        context = {"all_users": all_users}
        return render(request, "public_rating/leaderboard.html", context)


def contributor(request, user_id):
    if request.method == "GET":
        user = CoriandrumUser.objects.filter(vk_user_id=user_id)[0]
        if not user:
            return HttpResponse("404", status=404)
        context = {
            "user": user,
        }
        return render(request, "public_rating/contributor.html", context)