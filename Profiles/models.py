from django.contrib.auth.models import User
from django.db import models


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


class Friendship(models.Model):

    created = models.DateTimeField(auto_naddd=True,
                                   editable=False)

    creator = models.ForeignKey(UserProfile,
                                related_name="friendship_creator_set")

    friend = models.ForeignKey(UserProfile,
                               related_name="friend_set")

    def __unicode__(self):
        return "{} friends with {}".format(self.creator.user.username,
                                            self.friend.user.username)
