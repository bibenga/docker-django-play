import logging

from django.contrib.auth.models import User
from rest_framework import serializers

_l = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    resource_uri = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = User
        fields = ('resource_uri', 'id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('username',)
