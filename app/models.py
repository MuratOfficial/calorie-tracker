from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=264)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fats = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.PositiveIntegerField()
    image = models.ImageField(upload_to='foods_image', blank=True)

    def __str__(self):
        return self.name

class Stats(models.Model):
    food_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    carbs_full = models.DecimalField(max_digits=5, decimal_places=2)
    protein_full = models.DecimalField(max_digits=5, decimal_places=2)
    fats_full = models.DecimalField(max_digits=5, decimal_places=2)
    calories_full = models.PositiveIntegerField()
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stats
# Create your models here.
