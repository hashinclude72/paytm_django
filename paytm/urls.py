from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_payment, name='start_payment'),
    path('payment/', views.payment, name='payment'),
    path('response/', views.response, name='response'),

]
