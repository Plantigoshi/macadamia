from rest_framework import viewsets

from .models import Variable
from .serializer import VariableSerializer

from .modes import Value
from .serializers import ValueSerializer


class VariableViewSets(viewsets.ModelViewSet):

    serializer_class = VariableSerializer

    def get_queryset(self):
        return


class ValueViewSets(viewsets.ModelViewSet):

    serializers_class = ValueSerializer

    def get_queryset(self):
        return
