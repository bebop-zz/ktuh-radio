from music.models import Chart
from django.contrib import admin
from models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

# Create your views here.
def detail(request, music_id):
    chart = Chart.objects.get(pk=music_id)
    return render_to_response('music/detail.html',
    		{'chart': chart}, RequestContext(request, {}),)

def index(request):
    charts = Chart.objects.all()
    return render_to_response('music/index.html', 
                {'charts': charts}, RequestContext(request, {}),)
