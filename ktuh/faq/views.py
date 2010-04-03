from faq.models import Faq
from django.contrib import admin
from models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

# Create your views here.
def detail(request, faq_id):
    faq = Faq.objects.get(pk=faq_id)
    return render_to_response('faq/detail.html',
    		{'faq': faq}, RequestContext(request, {}),)

def index(request):
    faqs = Faq.objects.all()
    return render_to_response('faq/index.html', 
                {'faqs': faqs}, RequestContext(request, {}),)
