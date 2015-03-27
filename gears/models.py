from django.db import models

# Wing Model
class Wing(models.Model):
	brand = models.ForeignKey('Brand')
	pictures = models.ManyToManyField('gallery.Picture')
	designers = models.ManyToManyField('Designer')

	# Set a choice of wing types
	WING_TYPES = (
		('P', 'Paraglider'),
		('H', 'Hang glider'),
		('O', 'Other'),
	)
	wing_type = models.CharField(max_length=1, choices=WING_TYPES)

	name = models.CharField(max_length=50)
	area_flat = models.FloatField()
	area_proj = models.FloatField()
	span_flat = models.FloatField()
	span_proj = models.FloatField()
	aspect_ratio_flat = models.FloatField()
	aspect_ratio_proj = models.FloatField()
	cells = models.FloatField()
	total_line_length = models.FloatField()
	total_lines = models.FloatField()
	line_diameters = models.CharField(max_length=50)
	weight = models.FloatField()
	v_trim = models.FloatField()
	v_max = models.FloatField()
	en_category = models.CharField(max_length=50)
	takeoff_weight = models.FloatField()
	year = models.DateField()

class Brand(models.Model):
	designers = models.ManyToManyField('Designer')

	logo = models.ForeignKey('gallery.Picture')
	country = models.CharField(max_length=50)

class Designer(models.Model):
	user = models.ForeignKey('auth.User')

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)