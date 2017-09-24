from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Petition_info(models.Model):
	num=models.CharField(max_length=10)
	title=models.CharField(max_length=100)
	to_whom=models.CharField(max_length=100)
	what_is=models.CharField(max_length=200)
	desc=models.CharField(max_length=10240)
	img = models.ImageField(upload_to='images')
	signers=models.IntegerField()
	users=models.CharField(max_length=10240)


class User(models.Model):
	usernum=models.IntegerField()
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)