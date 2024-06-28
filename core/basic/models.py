from typing import Any
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

#Create
class Student(models.Model):
    #id = models.AutoField()  #automatically added by django if not defined and it is the primary key
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True)
    address = models.TextField()


class Car(models.Model):
    name=models.CharField(max_length=100)
    speed=models.IntegerField(default=100)

    def __str__(self) -> str:
        return self.name
    
@receiver(post_save, sender = Car)
def call_car_api(sender, instance, **kwargs):
    print("Car Object Created.")
    print(sender, instance, kwargs)