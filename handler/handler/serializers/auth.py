import logging

from django.contrib.auth import logout, login, authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from handler.serializers.user import UserSerializer

_l = logging.getLogger(__name__)


class PingSerializer(serializers.Serializer):
    user = UserSerializer()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(write_only=True, required=True, allow_blank=False, allow_null=False)
    user = UserSerializer(read_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        request = self.context['request']

        user = authenticate(request, username=username, password=password)
        if not user:
            raise ValidationError('invalid_login')
        if not user.is_active:
            raise ValidationError('inactive')

        login(request, user)

        attrs['user'] = request.user
        return attrs


class LogoutSerializer(serializers.Serializer):
    def validate(self, attrs):
        request = self.context['request']
        logout(request)
        attrs['user'] = request.user
        return attrs
