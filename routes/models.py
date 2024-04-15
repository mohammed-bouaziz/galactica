from django.db import models
from django.core.validators import MinValueValidator

class Routes(models.Model):
    origin = models.CharField(max_length=128, null=False, blank=False)
    destination = models.CharField(max_length=128, null=False, blank=False)
    travel_time = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.origin} to {self.destination} in {self.travel_time} days"


