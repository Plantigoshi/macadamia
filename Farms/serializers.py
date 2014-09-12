from rest_framework import serializers

from .models import Plant, Farm, PlantSpecie


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant


class FarmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm


class PlantSpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantSpecie
