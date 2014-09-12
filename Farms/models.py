from django.db import models


class Farm(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class PlantSpecie(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    temperature = models.DecimalField()
    humidity = models.DecimalField()
    light_intensity = models.DecimalField()

    def __unicode__(self):
        return self.name


class Plant(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    farm = models.ForeignKey(Farm)
    plant_specie = models.ForeignKey(PlantSpecie)

    def __unicode__(self):
        return self.name
