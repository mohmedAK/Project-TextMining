from django.utils import timezone

from django.db import models


# Create your models here.

class PersonData(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now())
    data = models.TextField()
    locationOfData = models.CharField(max_length=100)
    typeOfData = models.TextField()
    argument = models.TextField()

    def __str__(self):
        return self.name
