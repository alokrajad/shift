from django.contrib import admin
from .models import electric_vehicles,ShiftEvUploadExcel,colors_ev,choosable_options_ev
# Register your models here.
admin.site.register(electric_vehicles)
admin.site.register(colors_ev)

admin.site.register(choosable_options_ev)