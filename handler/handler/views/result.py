import logging

from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from handler.models import Sensor1Rule, Sensor2Rule, Result
from handler.serializers.result import ResultSerializer
from handler.serializers.sensor1 import Sensor1RuleSerializer
from handler.serializers.sensor2 import Sensor2RuleSerializer

_l = logging.getLogger(__name__)


class ResultFilter(filters.FilterSet):
    class Meta:
        model = Result
        fields = {
            'sensor': ('iexact', 'istartswith'),
            'source_id': ('iexact',),
            'code': ('iexact', 'istartswith'),
        }


class ResultViewSet(ReadOnlyModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Result.objects.all()
    filterset_class = ResultFilter
    serializer_class = ResultSerializer
    ordering_fields = ('sensor', 'source_id', 'code',)
    ordering = ('code',)
    search_fields = ('sensor', 'source_id', 'code',)

    @action(detail=False, methods=['DELETE'], serializer_class=Serializer)
    def clean(self, request, *args, **kwargs):
        Result.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

