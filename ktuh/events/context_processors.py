from django.conf import settings
from django.contrib.sites.models import Site
from events.models import Event
import datetime

def current_event(request):
    current_event = Event.objects.order_by('?')[0]
    return {
        'current_event': current_event,
    }
