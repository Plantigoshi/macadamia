from rest_framework import serializers

from .models import Plant
from .models import PlantSpecie
from .models import OptimalParameter

from Farms.serializers import FarmSerializer
from Profiles.serializers import ProfileSerializer


class PlantSpecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlantSpecie
        fields = ('id',
                  'name',
                  'plant_picture', )


class OptimalParameterSerializer(serializers.ModelSerializer):

    plant_specie = serializers.HyperlinkedRelatedField(many=True,
                                                       view_name='plantspecie-detail')

    class Meta:
        model = OptimalParameter
        fields = ('id',
                  'plant_specie',
                  'name',
                  'value', )


class PlantSerializer(serializers.ModelSerializer):

    plant_specie = PlantSpecieSerializer()
    owner = ProfileSerializer()
    farm = FarmSerializer()

    class Meta:
        model = Plant
        fields = ('id',
                  'name',
                  'owner',
                  'farm',
                  'plant_specie', )
