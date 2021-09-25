from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Place, Plant
from .serializers import CategorySerializer, PlaceSerializer, PlantSerializer
from rest_framework.response import Response

class PlantViewSet(viewsets.ModelViewSet):

    serializer_class = PlantSerializer

    def get_queryset(self):
        return Plant.objects.all()