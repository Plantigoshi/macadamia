from rest_framework import viewsets

from .models import Farm, Plant
from .serializers import FarmSerializer, PlantSerializer


class FarmViewSet(viewsets.ModelViewSet):

    serializer_class = FarmSerializer

    def get_queryset(self):
        return Farm.objects.filter(owner=self.request.user)


class PlantViewSet(viewsets.ModelViewSet):

    serializer_class = PlantSerializer

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)
