from django.db import models

# Create your models here.

class Rental(models.Model):
    name =  models.CharField(max_length=200)

class Reservation(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
