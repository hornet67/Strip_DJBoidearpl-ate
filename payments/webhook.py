import stripe
import traceback
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UserSubscription

@csrf_exempt
def stripe_webhook(request):
    """Handle Stripe webhook events"""
    
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    webhook_secret = settings.STRIPE_WEBHOOK_SECRET
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError as e:
        print(f"❌ Invalid payload: {e}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(f"❌ Invalid signature: {e}")
        return HttpResponse(status=400)
    
    # Handle the event
    event_type = event['type']
    event_data = event['data']['object']
    
    print(f"📨 Received event: {event_type}")
    
    if event_type == 'checkout.session.completed':
        try:
            # Use dictionary-style access (no .get())
            customer_email = event_data['customer_email'] if 'customer_email' in event_data else None
            customer_id = event_data['customer'] if 'customer' in event_data else None
            subscription_id = event_data['subscription'] if 'subscription' in event_data else None
            
            print(f"💰 Checkout completed for email: {customer_email}")
            
            if customer_email:
                try:
                    user = User.objects.get(email=customer_email)
                    print(f"✅ Found user: {user.username}")
                    
                    # Get or create subscription record
                    sub, created = UserSubscription.objects.get_or_create(user=user)
                    sub.is_active = True
                    sub.stripe_customer_id = customer_id
                    sub.stripe_subscription_id = subscription_id
                    sub.save()
                    print(f"🎉 Activated premium for {customer_email}")
                    
                except User.DoesNotExist:
                    print(f"❌ User not found: {customer_email}")
                except Exception as e:
                    print(f"❌ Database error: {e}")
                    traceback.print_exc()
            else:
                print("❌ No customer email in session")
                
        except Exception as e:
            print(f"❌ Error processing checkout: {e}")
            traceback.print_exc()
    
    elif event_type == 'customer.subscription.created':
        print(f"📋 Subscription created")
    
    elif event_type == 'invoice.paid':
        print(f"📄 Invoice paid")
    
    # Always return 200 to acknowledge receipt
    return HttpResponse(status=200)