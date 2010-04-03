from django.db import models

# Create your models here.
from django.db import models
from tinymce import models as tinymce_models
import datetime

class Chart(models.Model):
	chart_date = models.DateTimeField(blank=True, null=True)
	chart_reported_by = models.CharField(max_length=255)
	chart_chart = tinymce_models.HTMLField()
	chart_brief = tinymce_models.HTMLField()

	def __unicode__(self):
		return "Week of " + self.chart_date.strftime("%A, %d. %B %Y")
