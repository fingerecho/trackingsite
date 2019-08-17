from django.urls import path


from . import views
from  django.contrib import admin

urlpatterns = [
	path(r'admin/',admin.site.urls),
	path(r'index',views.index,name='index'),
]


