from django.db import models

class Cattle(models.Model):
    entrance_data = models.DateField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.id} :  * Current Weight -> {self.weight}  * Entrance Date -> {self.entrance_data} * Last Update Date -> {self.last_update}"

class Stable(models.Model):
    name = models.CharField(max_length=64)
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE, related_name="cattle")

    def __str__(self):
        return f"{self.id} has {self.cattle_id}"