from threading import local

from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin
from ipware import get_client_ip


_requests = local()


def get_current_request(silent=False):
    try:
        return _requests.request
    except AttributeError:
        if silent:
            return None
        raise


def get_current_user(silent=True):
    try:
        return _requests.request.user
    except AttributeError:
        if silent:
            return AnonymousUser()
        raise


class CommonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user_ip, _ = get_client_ip(request)

    def __call__(self, request):
        _requests.request = request
        try:
            return super().__call__(request)
        finally:
            if hasattr(_requests, 'request'):
                del _requests.request


class DoNotTrackMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.dnt = request.META.get('HTTP_DNT') == '1'
        # if request.user and request.user.is_authenticated:
        #     request.dnt = request.dnt or request.user.do_not_track
