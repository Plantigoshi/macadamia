from django.db import models

from Farms.models import Farm
from Profiles.models import UserProfile

from PIL import Image as ImagePIL
from PIL import ImageOps


def content_file_name(instance, filename):
    return '/'.join(['plants', instance.name])


class PlantSpecie(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120,
                            unique=True)
    plant_picture = models.ImageField(upload_to=content_file_name)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.image.url

    def save(self, *args, **kwargs):
        if not self.id and not self.plant_picture:
            return

        super(PlantSpecie, self).save()
        plant_picture = ImagePIL.open(self.plant_picture)
        plant_picture = ImageOps.fit(plant_picture,
                                     (640, 640), ImagePIL.ANTIALIAS)
        plant_picture.save(self.plant_picture.path, format= 'JPEG')


class OptimalParameter(models.Model):

    id = models.AutoField(primary_key=True)
    plant_specie = models.ForeignKey(PlantSpecie)
    name = models.CharField(max_length=120)
    value = models.FloatField()

    def __unicode__(self):
        return "{} with value {}".format(self.name,
                                         str(self.value))


class Plant(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(UserProfile)

    farm = models.ForeignKey(Farm,
                             null=True,
                             blank=True)

    plant_specie = models.ForeignKey(PlantSpecie)

    def __unicode__(self):
        return "{} is a {} with id {}".format(self.name,
                                              self.plant_specie.name,
                                              self.id)
