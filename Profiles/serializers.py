from django.contrib.auth.models import User

from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name',
                  'date_joined',
                  'last_login')


class NoDetailUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name', )


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    friends = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('id',
                  'user',
                  'profile_picture', )


class NoDetailProfileSerializer(serializers.ModelSerializer):

    user = NoDetailUserSerializer()

    class Meta:
        model = UserProfile
        fields = ('id',
                  'user',
                  'profile_picture', )
