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
    address = models.CharField(max_length = 20)
    dob = models.DateField()
    phone = models.CharField(max_length=10)


class hotel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length = 20)
    per_day_cost = models.FloatField()
    max_res = models.IntegerField()
    no_res = models.IntegerField()

    def update_res(self):
        if self.no_res < self.max_res:
            self.no_res +=1
            return True
        return False

class travel(models.Model):
    name = models.CharField(max_length = 20)
    rtc = models.FloatField()
    loc = models.CharField(max_length = 20)
    max_res = models.IntegerField()
    no_res = models.IntegerField()

    def update_res(self):
        if self.no_res < self.max_res:
            self.no_res +=1
            return True
        return False
        


class registeration(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)    
    hotel = models.ForeignKey(hotel, on_delete = models.CASCADE)
    travel = models.ForeignKey(travel, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    

