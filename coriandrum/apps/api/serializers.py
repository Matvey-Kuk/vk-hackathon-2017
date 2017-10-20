from rest_framework import serializers
from coriandrum.models import CoriandrumUser


class CoriandrumUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CoriandrumUser
        fields = ('vk_user_id', )
