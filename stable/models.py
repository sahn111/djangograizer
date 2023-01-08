from django.db import models

# Create your models here.

class Stable(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} : Name of stable is {self.name} its capacity is {self.capacity} and its address is {self.address}"
