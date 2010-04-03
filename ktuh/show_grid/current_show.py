from django.conf import settings
from django.contrib.sites.models import Site
from show_grid.models import ShowGrid, DJ, Show
import datetime

def current_show(request):
	try:
		date = datetime.datetime.now()
		day = date.weekday() + 1
		if day == 7:
			day = 0

		hour = date.hour
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
		if current_show:
			return {
				'current_show': current_show,
			}
		else:
			return {
				'' : ''
			}
	except Site.DoesNotExist:
		return {'':''} # an empty string
