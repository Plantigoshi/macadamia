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
                                     related_name='can_see')

    def __unicode__(self):
        return self.name


class PlantSpecie(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    plant_picture = models.ImageField(null=True,
                                      blank=True,
                                      upload_to=content_file_name)

    def __unicode__(self):
        return self.name


class OptimalParameter(models.Model):

    id = models.AutoField(primary_key=True)
    plant_specie = models.ForeignKey(PlantSpecie)
    name = models.CharField(max_length=120)
    value = models.FloatField()

    def __unicode__(self):
        return "{} on plant {}".format(self.name, self.plantSpecie.name)


class Plant(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(UserProfile)
    farm = models.ForeignKey(Farm)
    plant_specie = models.ForeignKey(PlantSpecie)

    def __unicode__(self):
        return self.name
