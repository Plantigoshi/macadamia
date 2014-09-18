from rest_framework import viewsets

from .models import Farm
from .serializers import FarmSerializer


class FarmViewSet(viewsets.ModelViewSet):

    serializer_class = FarmSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Farm.objects.filter(owner=self.kwargs['profile_pk'])
