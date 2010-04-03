from django.db import models

# Create your models here.
from django.db import models
from tinymce import models as tinymce_models
import datetime

class Faq(models.Model):
	faq_date = models.DateTimeField(blank=True, null=True)
	faq_title = models.CharField(max_length=255)
	faq_detail = tinymce_models.HTMLField()
	faq_brief = tinymce_models.HTMLField()

	def __unicode__(self):
		return self.faq_title
