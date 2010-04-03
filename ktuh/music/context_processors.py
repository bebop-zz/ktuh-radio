from django.conf import settings
from django.contrib.sites.models import Site
from music.models import Chart
import datetime

def current_chart(request):
    current_chart = Chart.objects.latest('chart_date')
    return {
        'current_chart': current_chart,
    }
