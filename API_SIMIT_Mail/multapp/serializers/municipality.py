from rest_framework import serializers
from multapp.models.municipality import Municipality


class MunicipalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipality
        fields = (
            'id',
            'dian_code',
            'name'
        )
        read_only_fields = (
            'id',
        )
