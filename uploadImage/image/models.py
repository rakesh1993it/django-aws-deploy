from django.db import models
from time import time
# from image.models import File

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

class Hotel(models.Model): 
	name = models.CharField(max_length=255) 
	ImagePath =models.CharField(max_length=255, null=True)
	# hotel_Main_Img = models.ImageField(upload_to='images/') 
	pub_date = models.DateTimeField( null=True)


class File(models.Model):
	name=models.CharField(max_length=255, null=True)
	file = models.FileField(blank=False, null=False)
	def __str__(self):
		return self.file.name

# https://www.techiediaries.com/django-rest-image-file-upload-tutorial/