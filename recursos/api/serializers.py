from rest_framework import serializers
from recursos import models

class RecursosSerializer(serializers.ModelSerializer):
    class Meta:
        data = serializers.DateTimeField(format="%d-%m-%Y")
        model = models.Recursos
        fields = '__all__'
