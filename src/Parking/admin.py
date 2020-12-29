from django.contrib import admin

# Register your models here.

from .models import Parking, Parking_Slot, Enforcer

admin.site.register(Parking)
admin.site.register(Parking_Slot)
admin.site.register(Enforcer)