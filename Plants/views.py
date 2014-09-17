from rest_framework import viewsets

from .models import PlantSpecie
from .serializers import PlantSpecieSerializer

from .models import OptimalParameter
from .serializers import OptimalParameterSerializer

from .models import Plant
from .models import PlantSerializer

class PlantSpecieViewSet(viewsets.ModelViewSet):

    model = PlantSpecie
    serializer_class = PlantSpecieSerializer


class OptimalParameterViewSet(viewsets.ModelViewSet):

    serializer_class = OptimalParameterSerializer

    def get_queryset(self):
        return OptimalParameter.objects \
                        .filter(plant_specie__id= \
                                self.kwargs['plantspecie_pk'])


class PlantViewSet(viewsets.ModelViewSet):

    serializer_class = PlantSerializer

    def get_queryset(self):
        return Plant.objects.filter(farm__id=self.kwargs['farm_pk'],
                                    owner__id=self.kwargs['profile_pk'])
