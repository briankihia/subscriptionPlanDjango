from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import initiate_payment
import json
from django.views.decorators.csrf import csrf_exempt
import logging

# Configure logging
logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['POST'])
def payment_callback(request):
    """
    Callback endpoint for M-Pesa payment notifications
    """
    try:
        # Parse the JSON body
        data = json.loads(request.body)
        
        # Extract STK callback data
        stk_callback = data.get('Body', {}).get('stkCallback', {})
        result_code = stk_callback.get('ResultCode')
        result_desc = stk_callback.get('ResultDesc')
        merchant_request_id = stk_callback.get('MerchantRequestID')
        checkout_request_id = stk_callback.get('CheckoutRequestID')

        logger.info("M-Pesa Callback Received:")
        logger.info(f"Result Code: {result_code}")
        logger.info(f"Result Description: {result_desc}")
        logger.info(f"Merchant Request ID: {merchant_request_id}")
        logger.info(f"Checkout Request ID: {checkout_request_id}")

        # If transaction was successful (ResultCode = 0)
        if result_code == 0:
            # Extract payment details from CallbackMetadata
            callback_items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            payment_data = {}
            
            # Process each item in the callback metadata
            for item in callback_items:
                name = item.get('Name')
                value = item.get('Value')
                payment_data[name] = value
            
            logger.info("Payment Details:")
            logger.info(f"Amount: {payment_data.get('Amount')}")
            logger.info(f"Receipt Number: {payment_data.get('MpesaReceiptNumber')}")
            logger.info(f"Transaction Date: {payment_data.get('TransactionDate')}")
            logger.info(f"Phone Number: {payment_data.get('PhoneNumber')}")
            
            # Here you can add code to update your database with the payment details
            
        else:
            logger.error(f"Payment failed with ResultCode: {result_code}")
            logger.error(f"Failure reason: {result_desc}")

    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {str(e)}")
        logger.error(f"Raw body: {request.body}")
    except Exception as e:
        logger.error(f"Error processing callback: {str(e)}")
    
    # Always return a success response to M-Pesa
    return JsonResponse({
        'ResultCode': 0,
        'ResultDesc': 'Callback received successfully'
    })

@csrf_exempt
@api_view(['POST'])
def initiate_mpesa_payment(request):
    try:
        data = json.loads(request.body)
        amount = data.get('amount')
        phone_number = data.get('phone_number')
        
        # Validate the required fields
        if not amount or not phone_number:
            return Response({
                'status': 'error',
                'message': 'Both amount and phone_number are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass the request object to get the current domain
        response = initiate_payment(amount, phone_number, request=request)
        
        return Response({
            'status': 'success',
            'data': response
        }, status=status.HTTP_200_OK)
        
    except json.JSONDecodeError:
        return Response({
            'status': 'error',
            'message': 'Invalid JSON in request body'
        }, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)