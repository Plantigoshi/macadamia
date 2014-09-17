from rest_framework import serializers

from .models import Farm
from Profiles.serializers import ProfileSerializer


class FarmSerializer(serializers.ModelSerializer):

    owner = ProfileSerializer()
    can_see = serializers.HyperlinkedRelatedField(many=True,
                                                  view_name='userprofile-detail')

    class Meta:
        model = Farm
        fields = ('id',
                  'name',
                  'owner',
                  'can_see', )
