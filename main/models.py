from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.IntegerField()
    detail = models.TextField()

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    hobbies = models.TextField()

class Employee2(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    department = models.TextField()


