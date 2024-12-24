from django.db import models

# Create your models here.

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    features = models.JSONField() # to store the list fo features

    def __str__(self):
        return self.name