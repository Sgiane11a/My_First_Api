from  .models import App
from rest_framework import viewsets, permissions
from .serializers import AppSerializer

class AppViewSet(viewsets.ModelViewSet):
   queryset  = App.objects.all() #conjunto de datos
   permission_classes = [permissions.AllowAny] #permiso para cualquier usuario

   serializer_class = AppSerializer #serializador que se va a usar