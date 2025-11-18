from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Refugio)
admin.site.register(Vacuna)
admin.site.register(Revision_Veterinaria)
admin.site.register(Animal)
admin.site.register(AnimalVacunas)
admin.site.register(Centro)