from django.db import models
from Car.models import Car
from django.contrib.auth.models import User

# Create your models here.
class Parking(models.Model):
    Parking_ID = models.AutoField(primary_key=True)
    Parking_Name = models.TextField(max_length=50, unique=True)
    Parking_Address = models.TextField(max_length=300)

    def __str__(self):
        return self.Parking_Name

class Parking_Slot(models.Model):
    STATUS = (
      (1, ('Free')),
      (2, ('Taken')),
      (3, ('Private')),
    )
    Slot_ID = models.AutoField(primary_key=True)
    Slot_number = models.IntegerField()
    Parking = models.ForeignKey(
        Parking,
        on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(
      choices=STATUS,
      default=1,
    )
    Taken_By = models.OneToOneField(
        Car,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
    )
    Rented_By = models.OneToOneField(
        User,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "%s - Slot %s" % (self.Parking.Parking_Name, self.Slot_number)

class Enforcer(models.Model):
    User = models.OneToOneField(
        User,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,)
    Parkings = models.ManyToManyField(Parking)

    def __str__(self):
        return "%s %s" % (self.User.first_name, self.User.last_name)
