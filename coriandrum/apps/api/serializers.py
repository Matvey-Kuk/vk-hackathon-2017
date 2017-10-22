from rest_framework import serializers
from coriandrum.models import CoriandrumUser, Post, PostAttachment


class CoriandrumUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CoriandrumUser
        fields = ("id",
                  "vk_user_id",
                  "vk_avatar",
                  "vk_name",
                  "n_all_posts",
                  "n_published",
                  "level",
                  "recently_leveled_up",
                  )


class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=False, queryset=CoriandrumUser.objects.all(), required=False)
    in_consideration_by_moderator = serializers.PrimaryKeyRelatedField(read_only=False, queryset=CoriandrumUser.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'status',
                  'raw_vk_attachments_payload', 'in_consideration_by_moderator')


class PostAttachmentSerializer(serializers.HyperlinkedModelSerializer):

    post = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Post.objects.all())

    class Meta:
        model = PostAttachment
        fields = ('id', 'post', 'raw_vk_attachment_payload')
