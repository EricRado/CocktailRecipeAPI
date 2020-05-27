from django.db import models

class Ingredient(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=30)
    thumbURL = models.URLField()