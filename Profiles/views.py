from rest_framework import viewsets

from .models import Friendship
from .models import UserProfile
#from .serializers import ProfileSerializer
from .serializers import FriendshipSerializer
from .serializers import NoDetailProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):

    model = UserProfile
    serializer_class = NoDetailProfileSerializer


class FriendshipViewSet(viewsets.ModelViewSet):

    serializer_class = FriendshipSerializer

    def get_queryset(self):
        return Friendship.objects.filter(creator__id=self.kwargs['profile_pk'])
