# we create an endpoint for our API

from django.urls import path, include
from .views import SubscriptionPlansView #this is the className
from .import views
from .mpesa.views import payment_callback

urlpatterns = [
    path('', views.home, name='home'),
    # we use .as_view() when we are using class based view in views
    # By using api/, you clearly separate the frontend routes (e.g., HTML pages) from the backend API routes (e.g., endpoints returning data in JSON format).
# This makes it easy to distinguish between routes that render HTML views for the user and those that serve data for other applications (such as mobile apps or other services).
    path('api/subscription-plans/', SubscriptionPlansView.as_view(), name='subscription-plans'),
    path('callback/', payment_callback, name='payment_callback'),
    path('api/mpesa/', include('plans.mpesa.urls', namespace='mpesa')),
]