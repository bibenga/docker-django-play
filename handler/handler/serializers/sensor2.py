import ast

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from handler.models import Sensor1Rule, Sensor2Rule


class Sensor2RuleSerializer(serializers.ModelSerializer):
    resource_uri = serializers.HyperlinkedIdentityField(view_name='sensor2rule-detail')

    class Meta:
        model = Sensor2Rule
        fields = ('resource_uri', 'id', 'code', 'value_expr')

    def validate(self, attrs):
        value_expr = attrs['value_expr']
        try:
            ast.parse(value_expr)
        except SyntaxError:
            raise ValidationError({'value2_expr': 'syntax error'})
        return attrs
