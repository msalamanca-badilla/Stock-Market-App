from django.db import models

# Create your models here.
class Symbol(models.Model):
    symbol = models.CharField(max_length=5)
