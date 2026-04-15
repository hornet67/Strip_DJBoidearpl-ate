from django.urls import path
from . import views
from . import webhook

urlpatterns = [
    path('pricing/', views.pricing, name='pricing'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
     path('webhook/stripe/', webhook.stripe_webhook, name='stripe_webhook'), 
]