from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	status = models.IntegerField(default=1)

	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	description = models.TextField()
	category = models.ForeignKey(Category)

	def __unicode__(self):
		return  " "+self.name+" : "+str(self.price)

class Stat(models.Model):
	category_count = models.IntegerField()

