from rest_framework import serializers

from .models import Plant, Farm, PlantSpecie
from Profiles.serializers import NoDetailProfileSerializer


class FarmSerializer(serializers.ModelSerializer):

    owner = NoDetailProfileSerializer()
    can_see = NoDetailProfileSerializer()

    class Meta:
        model = Farm


class PlantSpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantSpecie


class PlantSerializer(serializers.ModelSerializer):

    owner = NoDetailProfileSerializer()
    specie = PlantSpecie

    class Meta:
        model = Plant

