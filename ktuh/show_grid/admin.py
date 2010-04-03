from show_grid.models import Show, ShowGrid, DJ
from django.contrib import admin
from django.contrib.auth.models import User
from models import *

class ShowAdmin(admin.ModelAdmin):
	search_fields = ('show_name', 'show_blurb')

	def save_model(self, request, obj, form, change):
		obj.show_user = request.user
		obj.save()

	def queryset(self, request):
		qs = super(ShowAdmin, self).queryset(request)
		if not request.user.is_superuser:
			qs = qs.filter(show_user=request.user)
		return qs
 
class DJAdmin(admin.ModelAdmin):
	verbose_name = "DJ Profiles"
	verbose_name = "DJ Profile"
	verbose_name_plural = "DJ Profiles"
	search_fields = ['dj_user']
	list_display = ('dj_name', 'dj_current_show')
	
	def save_model(self, request, obj, form, change):
		obj.dj_user = request.user
		obj.save()

 	def queryset(self, request):
		qs = super(DJAdmin, self).queryset(request)
		if not request.user.is_superuser:
			qs = qs.filter(dj_user=request.user)
		return qs

class ShowGridAdmin(admin.ModelAdmin):
	list_display = ('showgrid_dj', 'showgrid_day')

admin.site.register(Show, ShowAdmin)
admin.site.register(DJ, DJAdmin)
admin.site.register(ShowGrid, ShowGridAdmin)

