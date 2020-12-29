from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    STATUS = (
      (1, ('Available')),
      (2, ('Unavailable')),
    )
    id = models.AutoField(primary_key=True)
    car_Name = models.TextField(max_length=50, unique=True)
    car_Model = models.TextField(max_length=50)
    car_licence_Plate = models.TextField(max_length=50)
    status = models.PositiveSmallIntegerField(
      choices=STATUS,
      default=1,
    )
    driver = models.OneToOneField(
        User,
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
    )
    cam_url = models.TextField(max_length=200)

    def __str__(self):
        return self.car_Name