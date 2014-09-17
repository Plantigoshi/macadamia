from django.db import models

from Profiles.models import UserProfile


def content_file_name(instance, filename):
    return '/'.join(['plants', instance.name])


class Farm(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    owner = models.ForeignKey(UserProfile,
                              related_name='owner')

    can_see = models.ManyToManyField(UserProfile,
                                     related_name='can_see',
                                     null=True,
                                     blank=True)

    def __unicode__(self):
        return self.name
