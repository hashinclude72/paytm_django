from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings



def start_payment(request):
    user = request.user

    return render(request, 'paytm/start_payment.html', {'title': 'start'})


def payment(request):
    user = request.user
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    order_id = Checksum.__id_generator__()     # Generating unique temporary id
    cust_id = user.username
    bill = 1
    mobile_no = '0987654321'
    email = user.email

    send_data = {
                'MID':MERCHANT_ID,
                'ORDER_ID':order_id,
                'CUST_ID': cust_id,
                'TXN_AMOUNT': bill,
                'CHANNEL_ID':'WEB',
                'WEBSITE': settings.PAYTM_WEBSITE,
                'MOBILE_NO': mobile_no,            #optional
                'EMAIL': email,                    #optional
                'INDUSTRY_TYPE_ID':'Retail',
                'CALLBACK_URL':CALLBACK_URL,
                # 'PAYMENT_MODE_ONLY':,               #optional
                # 'AUTH_MODE':,                       #optional
                # 'PAYMENT_TYPE_ID':,                 #optional
                # 'BANK_CODE':,                       #optional
            }
    paytm_data = send_data                           #remove it
    paytm_data['CHECKSUMHASH'] = Checksum.generate_checksum(send_data, MERCHANT_KEY)
    return render(request,"payments/paytm.html",{'paytmdict':paytm_data, 'user': user, 'title': 'Paytm'})


def response(request):
    pass
