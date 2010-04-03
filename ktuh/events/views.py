from events.models import Event
from django.contrib import admin
from models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

# Create your views here.
def detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render_to_response('events/detail.html',
    		{'event': event}, RequestContext(request, {}),)

def index(request):
    events = Event.objects.all()
    return render_to_response('events/index.html', 
                {'events': events}, RequestContext(request, {}),)
