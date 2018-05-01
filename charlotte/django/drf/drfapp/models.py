from django.db import models

# Create your models here.

class Breed(models.Model):
	
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=150)
	country = models.CharField(max_length=150)
	is_official = models.BooleanField(max_length=150)
	date_modified = models.DateTimeField(auto_now_add=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '{}'.format(self.name)

class Anime(models.Model):

	title = models.CharField(max_length=150)
	description = models.CharField(max_length=150)
	director = models.CharField(max_length=150)
	release_date = models.DateTimeField(auto_now_add=True)
	score = models.IntegerField()
	picture = models.ImageField(upload_to = 'static/media')
	date_modified= models.DateTimeField(auto_now_add=True)
	date_created = models.DateTimeField(auto_now_add=True)

class Website(models.Model):

	name = models.CharField(max_length=150)
	link = models.URLField()
	owner = models.CharField(max_length=150)
	logo = models.ImageField(upload_to= 'static/media')
	date_modified = models.DateTimeField(auto_now_add=True)
	date_created = models.DateTimeField(auto_now_add=True)

