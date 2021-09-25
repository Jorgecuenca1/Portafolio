from rest_framework import serializers
from .models import Category, Place, Plant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','image','name']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id','name','latitude','longitude']

class PlantSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    # Reverse FK relation
    place = PlaceSerializer(many=True)
    class Meta:
        model = Plant
        fields = ['id','image','name','scientific_name','description','category','place']