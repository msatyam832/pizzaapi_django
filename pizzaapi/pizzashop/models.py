from django.db import models

# Create your models here.
class Pizza(models.Model):
    types=models.CharField(max_length=50)
    toppings=models.CharField(max_length=100)
    size=models.CharField(max_length=100)



    def __str__(self):
        return self.types

