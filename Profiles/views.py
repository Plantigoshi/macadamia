from rest_framework import viewsets

from .models import UserProfile
from .serializers import ProfileSerializer
from .serializers import NoDetailProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):

    model = UserProfile
    serializer_class = NoDetailProfileSerializer
