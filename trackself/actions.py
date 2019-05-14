from django.contrib import messages


def show_visiter_city_action(modeladmin, request, queryset):
    for visiter in queryset:
    	visiter.location = 'helloworld'
    	visiter.save(update_fields="location")
    messages.info(request,"完成")
show_visiter_city_action.short_description = "显示Visiter的所在城市"