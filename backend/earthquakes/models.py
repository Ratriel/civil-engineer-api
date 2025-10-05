from django.db import models

class Earthquake(models.Model):
    date = models.DateField()
    time_local = models.TimeField()
    magnitude = models.FloatField()
    depth_km = models.FloatField()
    location_text = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    source = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    intensity = models.CharField(max_length=50, null=True, blank=True)
    event_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.date} {self.time_local} - M{self.magnitude} at {self.location_text}"
    
    