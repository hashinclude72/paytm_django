# Paytm Payments Gateway on Django (Python 3)
![Paytm](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Paytm_logo.png/150px-Paytm_logo.png) <img src="https://static.djangoproject.com/img/logos/django-logo-positive.png"  height="45">

### Paytm payments Gateway example.


Forked from here: [paytm-django](https://github.com/harishbisht/paytm-django)



## Quick Start
* First open your terminal and clone the project

```sh
git clone https://github.com/jaswal72/paytm_django.git
```
* Open Project directory
* Now install the requirements 
```sh
pip install -r requirements.txt
```
* Now go to payments ->settings.py and enter your credentials
```py
PAYTM_MERCHANT_KEY = '' # < your production KEY >
PAYTM_MERCHANT_ID = '' # < your production ID >
PAYTM_WEBSITE = 'DEFAULT'
PAYTM_URL = 'https://securegw.paytm.in/theia/processTransaction'
```
* Staging Credentials
```py
PAYTM_MERCHANT_KEY = 'GvYRwo%@Vl2Ml19y' # < your staging key >
PAYTM_MERCHANT_ID = 'BiDzIl44175596745392' # < your staging ID >
PAYTM_WEBSITE = 'WEBSTAGING'
PAYTM_URL = 'https://securegw-stage.paytm.in/theia/processTransaction'
```

* Make Migrations
```sh
python manage.py makemigrations
```

* Migrate paytm app for transactions details
```sh
python manage.py migrate
```

* Create Super user
```sh
python manage.py createsuperuser
```

* Now in terminal run the server and go to http://localhost:8000/
```
python manange.py runserver
```

* Go to

1. http://localhost:8000/admin
    - Log in using superuser credentials
2. http://localhost:8000/
    - Click Paytm Pay button to start payment

This should redirect you to Paytm Page.
Test Credentials to use for login:

> **Card:** <br>
>   Card Number : Any Visa or Master Card <br>
>   Expiration Month & Year : Any Future month and Year <br>
>   CVV : 123 <br>
>   OTP : 123123 <br>


> **Wallet:** <br>
>   Mobile Number : 7777777777 <br>
>   Password : Paytm12345 <br>
>   OTP: 489871 <br>

> **Net Banking:** <br>
>   Bank : Andhra Bank <br>
>   User : test <br>
>   Password : test <br>


### Paytm reference Documentation:

 * [Paytm Gateway Api Documentation](https://developer.paytm.com/docs/v1/payment-gateway) 
 * [Paytm Documentation](https://developer.paytm.com/docs) 
