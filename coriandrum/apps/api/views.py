from rest_framework import viewsets

from coriandrum.models import CoriandrumUser

from .serializers import CoriandrumUserSerializer


class CoriandrumUserViewSet(viewsets.ModelViewSet):
    queryset = CoriandrumUser.objects.all()
    serializer_class = CoriandrumUserSerializer
