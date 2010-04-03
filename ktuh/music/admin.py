from django.contrib import admin
from django.contrib.auth.models import User
from music.models import Chart
from models import *
import datetime


admin.site.register(Chart)
