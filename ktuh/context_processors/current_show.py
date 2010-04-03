from django.conf import settings
from django.contrib.sites.models import Site
from show_grid import ShowGrid, DJ, Show

def current_show(request):
	try:
		day = date.weekday()
		hour = datetime.hour
		if hour >= 0 and hour < 3:
			hour = 0
		elif hour >= 3 and hour < 6:
			hour = 3
		elif hour >= 6 and hour < 9:
			hour = 6
		elif hour >= 9 and hour < 12:
			hour = 9
		elif hour >= 12 and hour < 15:
			hour = 12
		elif hour >= 15 and hour < 18:
			hour = 15
		elif hour >= 18 and hour < 21:
			hour = 18
		elif hour >= 21 and hour < 24:
			hour = 21

		current_show = ShowGrid.objects.filter(showgrid_time=hour).filter(showgrid_day=day)
		return {
			'current_show': current_show,
		}
	except Site.DoesNotExist:
		return {'current_show':''} # an empty string
