from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from coriandrum.models import CoriandrumUser, Achievement, Post


def leaderboard(request):
    if request.method == "GET":
        all_users = list(CoriandrumUser.objects.all())
        all_users.sort(key=lambda u: len(u.published_posts), reverse=True)
        context = {"all_users": all_users}
        return render(request, "public_rating/leaderboard.html", context)


def entry(request):
    if request.method == "GET":
        vk_user_id = request.GET.get("viewer_id", "")
        viewer_type = int(request.GET.get("viewer_type", "0"))
        if viewer_type in [3, 4]:  # user is a community editor/admin
            return HttpResponseRedirect("/contributor/" + vk_user_id + "/admin")
        else: # user is not a member/is a regular member/is a moderator
            return HttpResponseRedirect("/contributor/" + vk_user_id)


def contributor(request, user_id, is_admin=False):
    if request.method == "GET":
        user_qs = CoriandrumUser.objects.filter(vk_user_id=user_id)
        if not user_qs:
            return render(request, "public_rating/newcomer.html")
        user = user_qs[0]
        context = {
            "user": user,
        }
        return render(request, "public_rating/contributor.html", context)


class IndexView(TemplateView):
    template_name = 'public_rating/newcomer.html'
