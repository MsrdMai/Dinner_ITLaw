
from django.db import models
from django.contrib.auth.models import User

class PageView(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0)

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone= models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    birthday = models.DateField(auto_now=False)


    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    school = models.CharField(max_length=50)
    cus_img = models.ImageField(upload_to='media')

