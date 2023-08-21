from django.db import models

# Create your models here.
class Dish(models.Model):
    dishName = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=8,decimal_places=2)
    available=models.BooleanField(default=True)

    def __str__(self):
        return f"Dish Name: {self.dishName} , Dish Price: {self.price}"



class Orders(models.Model):
    customer_name= models.CharField(max_length=100)
    dishes=models.ManyToManyField(Dish)
    status=models.CharField(max_length=30,default="Received")

