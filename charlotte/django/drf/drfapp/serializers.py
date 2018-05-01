from django.shortcuts import render
from rest_framework import serializers
from .models import Breed, Anime, Website
# Create your views here.

class BreedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Breed
		fields =('name', 'description', 'country', 'is_official', 'date_modified', 'date_created')

class AnimeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Anime
		fields = ('title', 'description', 'director', 'release_date', 'score', 'picture', 'date_modified', 'date_created')

class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Website
		fields = ('name', 'link', 'owner', 'logo', 'date_modified','date_created')
