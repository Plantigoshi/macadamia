from django.db import models

from Plants import Plant


class Variable(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    plant = models.ForeignKey(Plant)

    def __unicode__(self):
        return self.name

class Value(models.Model):

    id = models.AutoField(primary_key=True)
    variable = models.ForeignKey(Variable)
    value = models.FloatField()

    def __unicode__(self):
        return "{} with value {}".format(self.variable.name,
                                         self.value)
