from django.db import models
#from django.contrib.gis.db import models as geomodels

# Log Model (contain all infos related to a flight)
class Log(models.Model):
	pilot = models.ForeignKey('auth.User')
	track = models.ForeignKey('Track')
	gallery = models.ForeignKey('gallery.Gallery')
	wing = models.ForeignKey('gears.Wing')

	name = models.CharField(max_length=50)
	takeoff_date = models.DateField()
	landing_date = models.DateField()
	description = models.TextField()
	story = models.TextField()
	is_public = models.BooleanField(default=True)

# Track Model (contain all infos related to a track)
class Track(models.Model):
	filename = models.FileField()
	takeoff_point = models.ForeignKey('space.Point', related_name='takeoff_point')
	landing_point = models.ForeignKey('space.Point', related_name='landing_point')
	waypoints = models.ManyToManyField('space.Point', related_name='waypoints')
	is_GPS = models.BooleanField(default=False)

