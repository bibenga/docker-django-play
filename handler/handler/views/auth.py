from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from handler.serializers.auth import LogoutSerializer, LoginSerializer, PingSerializer
from handler.views.base import SimpleAPIView


class PingViewSet(ViewSet, SimpleAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PingSerializer

    def get_object(self):
        user = self.request.user
        return {
            'user': user if user.is_authenticated else None,
        }

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class LoginViewSet(ViewSet, SimpleAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer
    throttle_scope = 'login'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        user = self.request.user
        return {
            'username': None,
            'password': None,
            'user': user if user.is_authenticated else None,
        }

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class LogoutViewSet(ViewSet, SimpleAPIView):
    permission_classes = (AllowAny, )
    serializer_class = LogoutSerializer

    @method_decorator(sensitive_post_parameters())
    @method_decorator(ensure_csrf_cookie)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response()
