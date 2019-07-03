import logging

from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from handler.serializers.user import UserSerializer
from handler.views.base import TransactionModelViewSet

_l = logging.getLogger(__name__)


class UserViewSet(TransactionModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)
