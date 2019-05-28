from rest_framework import generics
from multapp.models.municipality import Municipality
from multapp.serializers.municipality import MunicipalitySerializer


class MunicipalityList(generics.ListCreateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    name = 'municipality-list'


class MunicipalityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    name = 'municipality-detail'
