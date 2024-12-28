# create an API endpoint that retrieves the subscription plans from the database


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SubscriptionPlan # this imports the normal data
from .serializers import SubscriptionPlanSerializer  #this imports the json data
from .mpesa.utils import initiate_payment



# Consistency: Using class-based views follows the DRF convention and allows for consistent code structure, especially in larger projects. It helps with readability and maintainability, particularly when handling more complex logic.
# In summary, class-based views provide a more scalable and structured approach to managing API endpoints compared to function-based views. They enable better organization of your code, especially when handling multiple HTTP methods and adding additional functionality down the line.

class SubscriptionPlansView(APIView):
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

def home(request):
    return render(request, 'home.html')
