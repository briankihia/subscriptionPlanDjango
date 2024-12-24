# this file is to convert the models data to json

from rest_framework import serializers
from .models import SubscriptionPlan

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['name', 'price', 'features']