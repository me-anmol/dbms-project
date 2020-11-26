from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    img = models.ImageField(upload_to='pics')
    per_day_cost = models.FloatField()
    no_of_visits = models.IntegerField()
    type_of_vacation = [
        ('Beach', 'Beach'),
        ('HillStation', 'HillStation'),
        ('safari', 'safari'),
        ('city', 'city'),
        ('International', 'International')
    ]
    type = models.CharField(max_length=100, choices=type_of_vacation)


class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    address = models.TextField()
    dob = models.DateField()
    phone = models.CharField(max_length=10)


