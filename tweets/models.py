from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Hashtag(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Twitter(models.Model):
	tweet = models.TextField()
	hashtag = models.CharField(max_length=20)
	account = models.CharField(max_length=20)

class Status(models.Model):
	text = models.TextField()
	user = models.ForeignKey(Account)
	created_at = models.CharField(max_length=100)
