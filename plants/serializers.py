from rest_framework import serializers
from .models import Category, Place, Plant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['image','name']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['name','latitude','logintude']

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['image','name','scientific_name','description','category','place']