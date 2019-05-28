from rest_framework import generics
from multapp.models.infraction import Infraction
from multapp.serializers.infraction import InfractionSerializer


class InfractionList(generics.ListCreateAPIView):
    queryset = Infraction.objects.all()
    serializer_class = InfractionSerializer
    name = 'infraction-list'


class InfractionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Infraction.objects.all()
    serializer_class = InfractionSerializer
    name = 'infraction-detail'
