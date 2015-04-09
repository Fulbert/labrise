from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Point(models.Model):
	name = models.CharField(max_length=50)
	coord = models.PointField()

	is_takeoff = models.BooleanField(default=False)
	is_landing = models.BooleanField(default=False)

	is_public = models.BooleanField(default=True)

	create_by = models.ForeignKey('auth.User')
	visible_by = models.ManyToManyField('auth.User',
										related_name='visible_by',
										null=True)

	objects = models.GeoManager()

	def __str__(self):
		return "{0} ({1})".format(self.name,self.coord)

class Address(models.Model):
	point = models.ForeignKey('Point',related_name="address_point")

class Track(models.Model):
	pass