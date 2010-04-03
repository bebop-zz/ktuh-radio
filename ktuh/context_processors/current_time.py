import datetime

def current_time(request):
	try:
		time = datetime.now()
		return {
			'current_time': time,
		}
	except Site.DoesNotExist:
		return {'current_time':''} # an empty string
