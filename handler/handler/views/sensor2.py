import logging

from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from handler.models import Sensor2Rule
from handler.serializers.sensor2 import Sensor2RuleSerializer

_l = logging.getLogger(__name__)


class Sensor2RuleFilter(filters.FilterSet):
    class Meta:
        model = Sensor2Rule
        fields = {
            'code': ('iexact', 'istartswith'),
        }


class Sensor2RuleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Sensor2Rule.objects.all()
    filterset_class = Sensor2RuleFilter
    serializer_class = Sensor2RuleSerializer
    ordering_fields = ('code',)
    ordering = ('code',)
    search_fields = ('code',)

