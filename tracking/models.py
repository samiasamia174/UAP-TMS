from django.db import models

# Create your models here.
from django.db import models


class Location(models.Model):
    bus = models.OneToOneField('transport.Bus', on_delete=models.CASCADE)

    lat = models.FloatField()
    lng = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bus} @ {self.lat},{self.lng}"
