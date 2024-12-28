import requests
from decouple import config
import base64
from datetime import datetime

# Get all environment variables
CONSUMER_KEY = config('MPESACONSUMERKEY')
CONSUMER_SECRET = config('MPESACONSUMERSECRETKEY')
BUSINESS_SHORTCODE = config('MPESABUSINESSSHORTCODE')
PASSKEY = config('MPESAPASSKEY')
CALLBACK = config('CALLBACK_DOMAIN')
ACCOUNT_REFERENCE = config('MPESAACCOUNTREFERENCE')

def get_daraja_access_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    auth = (CONSUMER_KEY, CONSUMER_SECRET)
    response = requests.get(url, auth=auth)
    access_token = response.json().get('access_token')
    return access_token

def generate_timestamp():
    return datetime.now().strftime('%Y%m%d%H%M%S')

def generate_password(timestamp):
    data_to_encode = f"{BUSINESS_SHORTCODE}{PASSKEY}{timestamp}"
    return base64.b64encode(data_to_encode.encode()).decode('utf-8')

def initiate_payment(amount, phone_number, request=None):
    access_token = get_daraja_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    timestamp = generate_timestamp()
    password = generate_password(timestamp)
    
    payload = {
        "BusinessShortCode": BUSINESS_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": BUSINESS_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": f"{CALLBACK}/api/mpesa/callback/",
        "AccountReference": ACCOUNT_REFERENCE,
        "TransactionDesc": "Payment for subscription"
    }

    payment_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    response = requests.post(payment_url, json=payload, headers=headers)
    return response.json()
