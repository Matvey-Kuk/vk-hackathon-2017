from django.conf.urls import url, include

from rest_framework import routers

from .views import CoriandrumUserViewSet

router = routers.DefaultRouter()
router.register(r'users', CoriandrumUserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]