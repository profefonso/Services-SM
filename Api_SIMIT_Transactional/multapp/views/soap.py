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

from multapp.models.municipality import Municipality


class MunicipalityComplex(ComplexModel):
    id = Integer
    dian_code = String
    name = String


class SoapService(ServiceBase):

    @rpc(Double(), Double(), _returns=Double)
    def suma(self, a, b):
        return a + b

    @rpc(_returns=Array(MunicipalityComplex))
    def list_municipality(self):
        list_m = Municipality.objects.values(
            'id',
            'dian_code',
            'name')
        return list_m

    @rpc(MunicipalityComplex, _returns=MunicipalityComplex)
    def add_municipality(self, municipality):
        data = municipality.as_dict()
        try:
            mun = Municipality.objects.create(**data)
            return Municipality.objects.filter(id=mun.id).values('id', 'dian_code', 'name').first()
        except IntegrityError as e:
            raise Fault(faultcode=str(e.args[0]), faultstring=e.args[1])

    @rpc(MunicipalityComplex, _returns=MunicipalityComplex)
    def edit_municipality(self, municipality):
        data = municipality.as_dict()
        try:
            Municipality.objects.filter(id=data['id']).update(**data)
            return Municipality.objects.filter(id=data['id']).values('id', 'dian_code', 'name').first()
        except IntegrityError as e:
            raise Fault(faultcode=str(e.args[0]), faultstring=e.args[1])

    @rpc(Integer, _returns=String)
    def delete_municipality(self, id):
        try:
            Municipality.objects.filter(id=id).delete()
            return 'Municipality '+str(id)+' as deleted'
        except ProtectedError as e:
            raise Fault(faultcode='400', faultstring=e.args[0])

    @rpc(Integer, _returns=MunicipalityComplex)
    def find_municipality(self, id):
        try:
            municipality = Municipality.objects.get(pk=id)
            return municipality
        except IntegrityError as e:
            raise Fault(faultcode=str(e.args[0]), faultstring=e.args[1])
        except Municipality.DoesNotExist:
            raise Fault(faultcode='404', faultstring=str('Municipality not exist'))


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)


def consulta():
    django_soap_app = DjangoApplication(soap_app)
    my_soap_app = csrf_exempt(django_soap_app)

    return my_soap_app
