from rest_framework import serializers

from handler.models import Result


class ResultSerializer(serializers.ModelSerializer):
    resource_uri = serializers.HyperlinkedIdentityField(view_name='result-detail')

    class Meta:
        model = Result
        fields = ('resource_uri', 'id', 'sensor', 'source_id', 'code', 'value', 'moment')

