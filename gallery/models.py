from django.db import models

# Gallery Model (contain all infos related to a gallery)
class Gallery(models.Model):
	owner = models.ManyToManyField('auth.User')

	name = models.CharField(max_length=50)
	description = models.TextField()


# Picture Model (contail all infos related to a gallery)
class Picture(models.Model):
	owner = models.ForeignKey('auth.User')

	picture = models.ImageField()

	name = models.CharField(max_length=50)
	description = models.TextField()
	is_public = models.BooleanField(default=True)
