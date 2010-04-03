from django.contrib import admin
from django.contrib.auth.models import User
from events.models import Event
from models import *
import datetime


admin.site.register(Event)
