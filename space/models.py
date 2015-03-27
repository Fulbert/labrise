from django.db import models


class Point(models.Model):
	name = models.CharField(max_length=50)
	coord = models.CharField(max_length=50)

	is_takeoff = models.BooleanField(default=False)
	is_landing = models.BooleanField(default=False)
