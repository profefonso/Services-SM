from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer, Double, String, DateTime, Date
from spyne.protocol.soap import Soap11, Soap12
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from spyne import Array
from spyne import ComplexModel
from django.db import IntegrityError
from spyne.model.fault import Fault
from django.db.models.deletion import ProtectedError
from multapp.utility.notification import SendMailNotifications

from multapp.models.infraction import Infraction


class InfractionComplex(ComplexModel):
    id = Integer
    date = DateTime
    road_type = String
    road_name = String
    location = String
    plate = String
    infraction_code = String
    vehicle_type = String
    vehicle_service = String
    offender_type = String
    offender_document_type = String
    offender_document_id = Integer
    offender_name = String
    offender_license_id = String
    offender_address = String
    offender_age = Integer
    offender_phone = String
    offender_mail = String
    owner_document_type = String
    owner_document_id = Integer
    owner_name = String
    company_id = String
    company_name = String
    transit_agent_name = String
    transit_agent_entity = String
    transit_agent_id = Integer
    transit_agent_observations = String
    document_url = String
    state = String
    state_date = Date


class InfractionManagementService(ServiceBase):

    @rpc(_returns=Array(InfractionComplex))
    def infraction_list(self):
        list_infractions = Infraction.objects.values(
            'id',
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
        return list_infractions

    @rpc(InfractionComplex, _returns=InfractionComplex)
    def add_infraction(self, infraction):
        data = infraction.as_dict()
        try:
            inf = Infraction.objects.create(**data)
            sendmailnotification = SendMailNotifications()
            sendmailnotification.send_mail(
                list_emails=[data['offender_mail']],
                subject='Multa de Transito - Simit Services',
                content_xml='<h2>Multa de Transito N0: ' + str(inf.id) +
                            '</h2></br><p>' +
                            'Estimado Infractor se ha creado una nueva Multa de Transito asociado al ciudadano ' +
                            str(inf.offender_document_id) + ' - ' + str(inf.offender_name) +
                            '</p></br><p>Realice el pago lo mas pronto posible para evitar sanciones</p>' +
                            '<br><h3>SIMIT Services</h3>'
            )
            return Infraction.objects.filter(id=inf.id).values(
                'id',
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
            ).first()
        except IntegrityError as e:
            raise Fault(faultcode=str(e.args[0]), faultstring=e.args[1])

    @rpc(InfractionComplex, _returns=InfractionComplex)
    def edit_infraction(self, infraction):
        data = infraction.as_dict()
        try:
            Infraction.objects.filter(id=data['id']).update(**data)
            return Infraction.objects.filter(id=data['id']).values(
                'id',
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
            ).first()
        except IntegrityError as e:
            raise Fault(faultcode=str(e.args[0]), faultstring=e.args[1])

    @rpc(Integer, _returns=String)
    def delete_infraction(self, id):
        try:
            Infraction.objects.filter(id=id).delete()
            return 'Infraction '+str(id)+' as deleted'
        except ProtectedError as e:
            raise Fault(faultcode='400', faultstring=e.args[0])

    @rpc(Integer, _returns=InfractionComplex)
    def find_infraction(self, id):
        try:
            infraction = Infraction.objects.get(pk=id)
            return infraction
        except IntegrityError as e:
            raise Fault(faultcode=str(e.args[0]), faultstring=e.args[1])
        except Infraction.DoesNotExist:
            raise Fault(faultcode='404', faultstring=str('Infraction not exist'))


soap_app = Application(
    [InfractionManagementService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)


def infraction_management():
    django_soap_app = DjangoApplication(soap_app)
    infraction_soap_app = csrf_exempt(django_soap_app)

    return infraction_soap_app
