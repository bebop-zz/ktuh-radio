from show_grid.models import Show, ShowGrid, DJ
from django.contrib import admin
from models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

def index(request):
	midnight = ShowGrid.objects.filter(showgrid_time=0).order_by('showgrid_day')
	three = ShowGrid.objects.filter(showgrid_time=3).order_by('showgrid_day')
	six = ShowGrid.objects.filter(showgrid_time=6).order_by('showgrid_day')
	nine = ShowGrid.objects.filter(showgrid_time=9).order_by('showgrid_day')
	noon = ShowGrid.objects.filter(showgrid_time=12).order_by('showgrid_day')
	fifteen = ShowGrid.objects.filter(showgrid_time=15).order_by('showgrid_day')
	eighteen = ShowGrid.objects.filter(showgrid_time=18).order_by('showgrid_day')
	twentyone = ShowGrid.objects.filter(showgrid_time=21).order_by('showgrid_day')
	return render_to_response(
		"show_grid/showgrid.html",
		{
		'midnight_list' : midnight,
		'three_list' : three,
		'six_list' : six,
		'nine_list' : nine,
		'noon_list' : noon,
		'fifteen_list' : fifteen,
		'eighteen_list' : eighteen,
		'twentyone_list' : twentyone,
		},        
		RequestContext(request, {}),
    )


def detail(request, show_grid_id):
    try:
        show = ShowGrid.objects.get(pk=show_grid_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('show_grid/detail.html',
    		{'show': show}, RequestContext(request, {}),)
