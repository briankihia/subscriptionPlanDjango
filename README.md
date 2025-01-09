# Subscription Plan with M-Pesa Integration

A Django-based subscription management system with Safaricom M-Pesa payment integration.

## Features
- Subscription plan management
- M-Pesa STK Push integration
- Payment callback handling
- Secure environment configuration

## Prerequisites
- Python 3.8+
- Django 3.1+
- PostgreSQL
- Safaricom Daraja API credentials
- ngrok (for local development)

## Installation


1. Clone the repository

2. Create and activate virtual environment
3.  Install dependencies

   
4. Environment Setup
- Copy `.env.example` to create your `.env` file:

- - Fill in the values in `.env` with your actual credentials:
  - Generate a new SECRET_KEY using:
    ```python
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```
  - Set up your database credentials
  -  - Add your M-Pesa API credentials from the Daraja portal

5. Database Setup

6. 
6. Run development server
7. 
## M-Pesa Integration Setup

### Daraja API Configuration
1. Create an account on [Safaricom Daraja Portal](https://developer.safaricom.co.ke/)
2. Create a new app to get your consumer key and secret
3. Set up your test credentials in `.env`:
   - MPESACONSUMERKEY
   - MPESACONSUMERSECRETKEY
   - MPESABUSINESSSHORTCODE
   - MPESAPASSKEY
   - 
### Local Development with ngrok
1. Install ngrok
2. Start ngrok tunnel:

3. 3. Update CALLBACK_DOMAIN in `.env` with your ngrok URL

## API Endpoints

### M-Pesa Payment
- Initiate Payment:
  - URL: `/api/mpesa/initiate/`
  - Method: POST
  - Body:
    ```json
    {
            "amount": "100",
        "phone_number": "254XXXXXXXXX"
    }
    ```

- Payment Callback:
  - URL: `/api/mpesa/callback/`
  - Method: POST
  - Handled automatically by the system

### Subscription Plans
- List Plans:
  - URL: `/api/subscription-plans/`
  - Method: GET

## Environment Variables
The following environment variables are required:


## Development
- The project uses Django's built-in development server
- PostgreSQL is used as the database
- Environment variables are managed using python-decouple
- API endpoints use Django REST Framework

## Security Notes
- Never commit `.env` file to version control
- Keep your M-Pesa API credentials secure
- Use HTTPS in production
- Set DEBUG=False in production

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
