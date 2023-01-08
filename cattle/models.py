from django.db import models

from stable.models import Stable
        
class Cattle(models.Model):
    entrance_data = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()
    stable = models.ForeignKey(Stable, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} has weight {self.weight} and its now inside of {self.stable.name} stable since {self.entrance_data}"
