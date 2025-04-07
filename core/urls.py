# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('payment/', views.payment_view, name='payment'),
    path('payment/success/<str:transaction_id>/', views.payment_success, name='payment_success'),
]