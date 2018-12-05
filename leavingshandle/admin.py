from django.contrib import admin

from .models import Leavings
# Register your models here.

class LeavingsAdmin(admin.ModelAdmin):
	list_display = ['email','content']
	fields = ['email','first_name','last_name','username','address','address2','content']


admin.site.register(Leavings,LeavingsAdmin)