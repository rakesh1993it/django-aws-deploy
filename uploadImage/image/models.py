from django.db import models
from time import time

# Create your models here.



def get_upload_file_name(instance, filename):
	return "images/%s_%s" % (str(time()).replace('.','_'), filename)


class Article(models.Model):
	title = models.CharField(max_length=200	)
	picture = models.FileField(upload_to= get_upload_file_name, blank=True, null=True)
	pub_date = models.DateTimeField('date_published', null=True)
	
	def __unicode__(self):
		return self.title
   
	def get_absolute_url(self):
		return "/artimages/get/%i/" % self.id