from django.db import models

# Create your models here.

class Visiter(models.Model):

	FRIENDS_SIZE = (
		('0','Customer'),
		('1','Friends'),
		('2','myself')
	)
	id = models.AutoField(primary_key=True)
	last_time_visit  = models.DateTimeField(auto_now=True,verbose_name="最近到访时间")
	first_time_visit = models.DateTimeField(auto_now=False,blank=False,verbose_name="首次到访时间")
	friend_status = models.CharField(max_length=1,choices=FRIENDS_SIZE,blank=False,verbose_name="属性")
	visit_times = models.IntegerField(default=1,blank=False,verbose_name="访问次数")
	tokens = models.CharField(max_length=256,blank=False,default="---**---")
	location = models.CharField(max_length=128,blank=True,verbose_name="地理位置")
	device = models.CharField(max_length=64,blank=True,verbose_name="设备")
	os = models.CharField(max_length=64,blank=True,verbose_name="操作系统")
	browser = models.CharField(max_length=64,blank=True,verbose_name="浏览器")
	casual_user = models.BooleanField(blank=False,default=True,verbose_name="随意浏览?")
	ip = models.GenericIPAddressField(blank=False,default="192.168.1.1",verbose_name="ip")
	isp = models.CharField(max_length=128,blank=True,verbose_name="运营商")
	uuid = models.UUIDField(max_length=64,blank=True,default="dc09c995-30a2-4d42-8ecf-8b1a9d96e0af")
	def __str__(self):
		return "visiter_%d"%self.id
	class Meta:
		#db_table = "visiter"
		verbose_name = "到访者"

class Pageview(models.Model):
	id = models.AutoField(primary_key=True)
	random = models.CharField(max_length=64,default='0')
	visiter = models.ForeignKey(Visiter,to_field='id',on_delete=models.CASCADE,verbose_name="访客")
	brow_page = models.CharField(max_length=64,default="-",verbose_name="浏览页面")
	referer = models.CharField(max_length=256,default="-",verbose_name="来路")
	language = models.CharField(max_length=64,default="-",verbose_name="语言")
	residencetime = models.CharField(max_length=32,blank=True,default="-0.1",verbose_name="停留时间")
	platform = models.CharField(max_length=64,default='-',verbose_name="平台")
	screen = models.CharField(max_length=16,default='-',verbose_name="屏幕")
	def __str__(self):
		return "pageview_%d"%self.id
	class Meta:
		#db_table = "pageview"
		verbose_name = "请求"
