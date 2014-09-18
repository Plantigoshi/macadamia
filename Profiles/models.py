from django.contrib.auth.models import User
from django.db import models

from PIL import Image as ImagePIL
from PIL import ImageOps


def content_file_name(instance, filename):
    return '/'.join(['profile', instance.user.username, 'picture'])


class UserProfile(models.Model):

    user = models.OneToOneField(User,
                                related_name='user')

    profile_picture = models.ImageField(null=True,
                                        blank=True,
                                        upload_to=content_file_name,
                                        default='profile/default/picture.jpg')

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return self.image.url

    def save(self, *args, **kwargs):
        if not self.id and not self.profile_picture:
            return

        super(UserProfile, self).save()
        profile_picture = ImagePIL.open(self.profile_picture)
        profile_picture = ImageOps.fit(profile_picture,
                                       (640, 640), ImagePIL.ANTIALIAS)
        profile_picture.save(self.profile_picture.path, format= 'JPEG')


class Friendship(models.Model):

    created = models.DateTimeField(auto_now_add=True,
                                   editable=False)

    creator = models.ForeignKey(UserProfile,
                                related_name="friendship_creator_set")

    friend = models.ForeignKey(UserProfile,
                               related_name="friend_set")

    def __unicode__(self):
        return "{} friends with {}".format(self.creator.user.username,
                                            self.friend.user.username)
