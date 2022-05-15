from django.db import models
import datetime


# Create your models here.
class Recursos(models.Model):
    nome = models.CharField(max_length=50)
    qtd = models.IntegerField()
    data = models.DateField(default=datetime.date.today)