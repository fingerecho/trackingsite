from django.contrib import admin

from .models  import Visiter , Pageview
from .actions import show_visiter_city_action

class VisiterAdmin(admin.ModelAdmin):
	#list_display = ('first_visit_time','last_visit_time','visit_times','tokens')
	fields = ['ip','location','isp','first_time_visit','last_time_visit','visit_times','tokens','friend_status','device','browser','os']
	list_display = ['friend_status','ip','location','isp','visit_times','casual_user','first_time_visit','last_time_visit','device','os','browser',]
	actions = [show_visiter_city_action]
	pass

class PageviewAdmin(admin.ModelAdmin):
	list_display = ['residencetime','brow_page','referer','language']
	#fields = ['residencetime','brow_page','referer','language']
	exclude  = []
	pass


admin.site.register(Visiter,VisiterAdmin)
admin.site.register(Pageview,PageviewAdmin)
#admin.site.register([Visiter,])

