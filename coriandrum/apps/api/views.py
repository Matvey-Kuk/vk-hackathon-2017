from rest_framework import viewsets

from coriandrum.models import CoriandrumUser, Post, PostAttachment

from .serializers import CoriandrumUserSerializer, PostSerializer, PostAttachmentSerializer


class CoriandrumUserViewSet(viewsets.ModelViewSet):
    lookup_field = 'vk_user_id'
    queryset = CoriandrumUser.objects.all()
    serializer_class = CoriandrumUserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAttachmentViewSet(viewsets.ModelViewSet):
    queryset = PostAttachment.objects.all()
    serializer_class = PostAttachmentSerializer
