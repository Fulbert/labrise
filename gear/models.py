from django.db import models


class Gear(models.Model):
	gear_type = models.ForeignKey('GearType',blank=True,null=True)

	brand = models.ForeignKey('Brand')
	pictures = models.ImageField(blank=True,null=True)
	designers = models.ManyToManyField('Designer',blank=True,null=True)
	datas = models.ManyToManyField('GearData',blank=True,null=True)

	name = models.CharField(max_length=50)
	size = models.CharField(max_length=50)

	def __str__(self):
		return "[{0.gear_type}] {0.brand} {0.name} {0.size}".format(self)	

class GearType(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class GearDataType(models.Model):
	gear_type = models.ForeignKey('GearType',blank=True,null=True)
	data_name = models.CharField(max_length=50)

	def __str__(self):
		return "[{0.gear_type}] {0.data_name}".format(self)

class GearData(models.Model):
	data_type = models.ForeignKey('GearDataType',blank=True,null=True)
	value = models.CharField(max_length=50)

	def __str__(self):
		return "{0.data_type}: {0.value}".format(self)

class Brand(models.Model):
	name = models.CharField(max_length=50)
	designers = models.ManyToManyField('Designer',null=True,blank=True)

	logo = models.ImageField(null=True,blank=True)
	country = models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.name

class Model(models.Model):
	name = models.CharField(max_length=50)

	datas = models.ManyToManyField('GearData',blank=True,null=True)

	def __str__(self):
		return self.name

class Designer(models.Model):
	member = models.ForeignKey('member.Member',null=True,blank=True)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)