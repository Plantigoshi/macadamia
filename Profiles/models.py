from django.contrib.auth.models import User
from django.db import models

def content_file_name(instance, filename):
    return '/'.join(['profile', instance.user.username, 'picture'])


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    profile_picture = models.ImageField(null=True,
                                        blank=True,
                                        upload_to=content_file_name,
                                        default='profile/default/picture.jpg')

    def __unicode__(self):
        return self.user.username
