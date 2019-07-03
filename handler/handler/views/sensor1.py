import logging

from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from handler.models import Sensor1Rule
from handler.serializers.sensor1 import Sensor1RuleSerializer

_l = logging.getLogger(__name__)


class Sensor1RuleFilter(filters.FilterSet):
    class Meta:
        model = Sensor1Rule
        fields = {
            'code': ('iexact', 'istartswith'),
        }


class Sensor1RuleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Sensor1Rule.objects.all()
    filterset_class = Sensor1RuleFilter
    serializer_class = Sensor1RuleSerializer
    ordering_fields = ('code',)
    ordering = ('code',)
    search_fields = ('code',)

