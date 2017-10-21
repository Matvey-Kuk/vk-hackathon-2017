from django.conf.urls import url, include

from rest_framework import routers

from .views import CoriandrumUserViewSet, PostViewSet, PostAttachmentViewSet

router = routers.DefaultRouter()
router.register(r'users', CoriandrumUserViewSet)
router.register(r'post', PostViewSet)
router.register(r'post_attachment', PostAttachmentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
