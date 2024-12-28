from django.urls import path
from . import views

app_name = 'mpesa'  # Make sure this is present

urlpatterns = [
    path('initiate/', views.initiate_mpesa_payment, name='initiate-mpesa-payment'),
    path('callback/', views.payment_callback, name='mpesa-callback'),
] 