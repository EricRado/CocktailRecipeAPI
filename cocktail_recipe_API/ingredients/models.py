from django.db import models
import uuid

class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=30)
    thumbURL = models.URLField()

    class Meta:
        db_table = "ingredient"
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"