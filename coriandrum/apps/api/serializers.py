from rest_framework import serializers
from coriandrum.models import CoriandrumUser, Post


class CoriandrumUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoriandrumUser
        fields = ('id', 'vk_user_id', "vk_avatar", "vk_name")


class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=False, queryset=CoriandrumUser.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'author', 'text')
