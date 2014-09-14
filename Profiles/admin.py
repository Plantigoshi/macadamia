from django.contrib import admin

from .models import UserProfile
from .models import Friendship

admin.site.register(UserProfile)
admin.site.register(Friendship)
