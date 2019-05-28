from django.db import models
from .municipality import Municipality


class Infraction(models.Model):
    date_created = models.DateField(
        auto_now_add=True
    )

    date = models.DateTimeField(
        auto_now_add=False
    )

    AV = 'AV'
    CLL = 'CLL'
    CR = 'CR'

    ROAD_CHOICES = (
        (AV, AV),
        (CLL, CLL),
        (CR, CR),
    )

    road_type = models.CharField(
        max_length=15,
        choices=ROAD_CHOICES,
        default=AV
    )

    road_name = models.CharField(
        max_length=255
    )

    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=255
    )

    plate = models.CharField(
        max_length=10
    )

    infraction_code = models.CharField(
        max_length=10
    )

    vehicle_type = models.CharField(
        max_length=255
    )

    vehicle_service = models.CharField(
        max_length=255
    )

    DRIVER = 'driver'
    WALKER = 'walker'
    PASSENGER = 'Passenger'

    OFFENDER_CHOICES = (
        (DRIVER, DRIVER),
        (WALKER, WALKER),
        (PASSENGER, PASSENGER),
    )

    offender_type = models.CharField(
        max_length=15,
        choices=OFFENDER_CHOICES,
        default=DRIVER
    )

    CC = 'CC'
    TI = 'TI'
    CE = 'CE'
    PASAPORTE = 'PASAPORTE'

    DOCUMENTS_CHOICES = (
        (CC, CC),
        (TI, TI),
        (CE, CE),
        (PASAPORTE, PASAPORTE)
    )

    offender_document_type = models.CharField(
        max_length=10,
        choices=DOCUMENTS_CHOICES,
        default=CC
    )

    offender_document_id = models.BigIntegerField()

    offender_name = models.CharField(
        max_length=255
    )

    offender_license_id = models.CharField(
        max_length=100
    )

    offender_address = models.CharField(
        max_length=255
    )

    offender_age = models.IntegerField()

    offender_phone = models.CharField(
        max_length=50
    )

    offender_mail = models.CharField(
        max_length=255
    )

    owner_document_type = models.CharField(
        max_length=10,
        choices=DOCUMENTS_CHOICES,
        default=CC
    )

    owner_document_id = models.BigIntegerField()

    owner_name = models.CharField(
        max_length=255
    )

    company_id = models.CharField(
        max_length=100
    )

    company_name = models.CharField(
        max_length=255
    )

    transit_agent_name = models.CharField(
        max_length=255
    )

    transit_agent_entity = models.CharField(
        max_length=255
    )

    transit_agent_id = models.BigIntegerField()

    transit_agent_observations = models.CharField(
        max_length=255
    )

    document_url = models.CharField(
        max_length=255
    )

    CREATED = 'created'
    ACTIVE = 'active'
    REJECTED = 'rejected'
    PAID = 'paid'

    STATES_CHOICES = (
        (CREATED, CREATED),
        (ACTIVE, ACTIVE),
        (REJECTED, REJECTED),
        (PAID, PAID)
    )

    state = models.CharField(
        max_length=15,
        choices=STATES_CHOICES,
        default=ACTIVE
    )

    state_date = models.DateTimeField(
        auto_now_add=False,
        null=True
    )

    def __str__(self):
        return str(self.date_created) + ' - ' + str(self.id)
