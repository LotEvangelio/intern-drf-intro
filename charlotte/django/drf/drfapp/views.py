from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .models import Breed,Anime,Website
from drfapp.serializers import BreedSerializer, AnimeSerializer, WebsiteSerializer
# Create your views here.

class BreedViewSet(viewsets.ModelViewSet):
	queryset =Breed.objects.all()
	serializer_class = BreedSerializer

class AnimeViewSet(viewsets.ModelViewSet):
	queryset =Anime.objects.all()
	serializer_class = AnimeSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
	queryset= Website.objects.all()
	serializer_class = WebsiteSerializer