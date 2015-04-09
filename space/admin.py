from django.contrib.gis import admin
from space.models import Point

admin.site.register(Point, admin.OSMGeoAdmin)