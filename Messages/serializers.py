from rest_framework import serializers

from .models import Variable
from .models import Value


class VariableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variable


class ValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Value
