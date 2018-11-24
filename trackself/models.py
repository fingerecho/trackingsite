from django.db import models

# Create your models here.

class Visiter(models.Model):
	FRIENDS_SIZE = (
		('0','Customer'),
		('1','Friends'),
		('2','myself')
	)

	first_time_visit = models.CharField(max_length=20)
	last_time_visit  = models.CharField( max_length=20,blank = True )
	friend_status = models.CharField(max_length=1,choices=FRIENDS_SIZE)
	visit_times = models.IntegerField(default=1)
	tokens = models.CharField(max_length=256)
	location = models.CharField(max_length=128,blank=True)
	device = models.CharField(max_length=64)
	os = models.CharField(max_length=64)
	browser = models.CharField(max_length=64)
	brows_pages = models.CharField(max_length=64,default="*")
	casual_user = models.BooleanField(default=True)
	ip = models.GenericIPAddressField(default="0x00")
	isp = models.CharField(max_length=128,blank=True)

