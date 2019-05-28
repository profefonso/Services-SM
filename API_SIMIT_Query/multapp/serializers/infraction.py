from rest_framework import serializers
from multapp.models.infraction import Infraction


class InfractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Infraction
        fields = (
            'id',
            'date_created',
            'date',
            'road_type',
            'road_name',
            'municipality',
            'location',
            'plate',
            'infraction_code',
            'vehicle_type',
            'vehicle_service',
            'offender_type',
            'offender_document_type',
            'offender_document_id',
            'offender_name',
            'offender_license_id',
            'offender_address',
            'offender_age',
            'offender_phone',
            'offender_mail',
            'owner_document_type',
            'owner_document_id',
            'owner_name',
            'company_id',
            'company_name',
            'transit_agent_name',
            'transit_agent_entity',
            'transit_agent_id',
            'transit_agent_observations',
            'document_url',
            'state',
            'state_date'
        )
        read_only_fields = (
            'id',
        )
