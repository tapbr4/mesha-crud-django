from rest_framework import viewsets
from recursos.api import serializers
from recursos import models

class RecursosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecursosSerializer
    queryset = models.Recursos.objects.all()