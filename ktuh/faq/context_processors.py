from django.conf import settings
from django.contrib.sites.models import Site
from faq.models import Faq
import datetime

def current_faq(request):
    current_faq = Faq.objects.order_by('?')[0]
    return {
        'current_faq': current_faq,
    }
