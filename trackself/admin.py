from django.contrib import admin

from .models  import Visiter

class VisiterAdmin(admin.ModelAdmin):
	#list_display = ('first_visit_time','last_visit_time','visit_times','tokens')
	fields = ['brows_pages','ip','location','isp','first_time_visit','last_time_visit','visit_times','tokens','friend_status','device','browser','os']
	list_display = ['friend_status','ip','location','isp','visit_times','brows_pages','casual_user','first_time_visit','last_time_visit','device','os','browser',]
	pass

admin.site.register(Visiter,VisiterAdmin)
#admin.site.register([Visiter,])

