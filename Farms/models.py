from django.db import models

from Profiles.models import UserProfile


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
    temperature = models.FloatField()
    humidity = models.FloatField()
    light_intensity = models.FloatField()

    def __unicode__(self):
        return self.name


class Plant(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(UserProfile)
    farm = models.ForeignKey(Farm)
    plant_specie = models.ForeignKey(PlantSpecie)

    def __unicode__(self):
        return self.name
