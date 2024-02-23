from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.TextField()
    ingredients_list = models.TextField()
    difficulty = models.TextField()

    def __str__(self):
        return str(self.name)