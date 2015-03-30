from django.contrib import admin
from flightlog.models import Log, Track, Trip

admin.site.register(Log)
admin.site.register(Track)
admin.site.register(Trip)