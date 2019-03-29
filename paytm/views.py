from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import Checksum
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Paytm_history



@login_required
def start_payment(request):

    return render(request, 'paytm/start_payment.html')

@login_required
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
                'MERC_UNQ_REF':user.id,               #used to save data in response
                # 'PAYMENT_MODE_ONLY':,               #optional
                # 'AUTH_MODE':,                       #optional
                # 'PAYMENT_TYPE_ID':,                 #optional
                # 'BANK_CODE':,                       #optional
                # see documentation https://developer.paytm.com/docs/v1/payment-gateway
            }
    paytm_data = send_data
    paytm_data['CHECKSUMHASH'] = Checksum.generate_checksum(send_data, MERCHANT_KEY)
    return render(request,"paytm/payment.html",{'paytmdict':paytm_data, 'user': user})


@csrf_exempt
def response(request):
    if request.method == "POST":
        user = request.user
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        data_dict = dict(request.POST.items())

        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            for key in request.POST:
                if key == "BANKTXNID" or key == "RESPCODE":
                    if request.POST[key]:
                        data_dict[key] = int(request.POST[key])
                    else:
                        data_dict[key] = 0
                elif key == "TXNAMOUNT":
                    data_dict[key] = float(request.POST[key])
            Paytm_history.objects.create(user_id = data_dict['MERC_UNQ_REF'], **data_dict)                 #saving data
            return render(request, "paytm/response.html", {"paytm":data_dict, 'user': user})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)
