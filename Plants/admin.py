from django.contrib import admin

from .models import Plant
from .models import PlantSpecie
from .models import OptimalParameter


admin.site.register(Plant)
admin.site.register(PlantSpecie)
admin.site.register(OptimalParameter)
