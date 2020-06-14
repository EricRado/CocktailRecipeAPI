from django.db import models
import uuid

class Drink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=30)
    IBA = models.CharField(max_length=120)
    alcoholic = models.CharField(max_length=30)
    glass = models.CharField(max_length=50)
    instructions = models.TextField()
    thumbURL = models.URLField()
    ingredient1 = models.CharField(max_length=50)
    ingredient2 = models.CharField(max_length=50) 
    ingredient3 = models.CharField(max_length=50)
    ingredient4 = models.CharField(max_length=50)
    ingredient5 = models.CharField(max_length=50)
    ingredient6 = models.CharField(max_length=50)
    ingredient7 = models.CharField(max_length=50)
    ingredient8 = models.CharField(max_length=50)
    measure1 = models.CharField(max_length=15)
    measure2 = models.CharField(max_length=15)
    measure3 = models.CharField(max_length=15)
    measure4 = models.CharField(max_length=15)
    measure5 = models.CharField(max_length=15)
    measure6 = models.CharField(max_length=15)
    measure7 = models.CharField(max_length=15)
    measure8 = models.CharField(max_length=15)

    class Meta:
        db_table = "drink"
        verbose_name = "Drink"
        verbose_name_plural = "Drinks"

class DrinkSlim(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    thumbURL = models.URLField()

    class Meta:
        db_table = "drink_slim"
        verbose_name = "DrinkSlim"
        verbose_name_plural = "DrinkSlims"