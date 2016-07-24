from django.db import models
from django.utils import timezone

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    element = models.CharField(max_length=20)
    weakness = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    height = models.FloatField
    weight = models.FloatField
    def publish(self):
        self.save()
    def __str__(self):
        return self.name
    
