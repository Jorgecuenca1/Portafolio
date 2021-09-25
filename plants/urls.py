from rest_framework import routers
from .views import PlantViewSet

routera = routers.SimpleRouter()
routera.register(r'plant', PlantViewSet, basename='plant'),