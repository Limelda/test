from django.db import models
from django.utils import timezone
from plist.choices import *

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    element = models.CharField(choices=ELEMENTS, max_length=20)
    weakness = models.CharField(max_length=20, choices=ELEMENTS)
    created_date = models.DateTimeField(default=timezone.now)
    def publish(self):
        self.save()
    def __str__(self):
        return self.name
