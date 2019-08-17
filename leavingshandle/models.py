from django.db import models


class Leavings(models.Model):
	first_name = models.CharField(max_length=64,blank=True)
	last_name = models.CharField(max_length=64,blank=True)
	username = models.CharField(max_length=128,blank=True)
	email = models.CharField(max_length=128)
	address = models.CharField(max_length=512,blank=True)
	address2 = models.CharField(max_length=512,blank=True)
	content = models.CharField(max_length=1024*2*2,blank=True)
	#subtime = models.DateField()



