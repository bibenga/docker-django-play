from django.db import transaction
from django.http import Http404
from rest_framework.permissions import SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class SimpleAPIView(APIView):
    serializer_class = None

    def get_queryset(self):
        return []

    def get_object(self):
        raise Http404

    def get_serializer(self, *args, **kwargs):
        # serializer_class = self.get_serializer_class()
        serializer_class = kwargs.pop('serializer_class', None) or self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )

        return self.serializer_class

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }


class TransactionMixin(APIView):
    def dispatch(self, request, *args, **kwargs):
        if request.method in SAFE_METHODS:
            return super().dispatch(request, *args, **kwargs)

        with transaction.atomic():
            return super().dispatch(request, *args, **kwargs)


class TransactionSimpleAPIView(TransactionMixin, SimpleAPIView):
    pass


class TransactionModelViewSet(TransactionMixin, ModelViewSet):
    pass
