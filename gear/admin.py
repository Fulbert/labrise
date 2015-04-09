from django.contrib import admin
from gear.models import Gear, GearType, GearData, GearDataType, Brand, Designer


admin.site.register(Gear)
admin.site.register(GearType)
admin.site.register(GearData)
admin.site.register(GearDataType)
admin.site.register(Brand)
admin.site.register(Designer)