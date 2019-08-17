


def show_visiter_city_action(modeladmin, request, queryset):
    for visiter in queryset:
    	visiter.location = 'helloworld'

show_visiter_city_action.short_description = "显示Visiter的所在城市"