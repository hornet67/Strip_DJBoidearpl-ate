import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Set Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def pricing(request):
    """Display pricing page"""
    return render(request, 'payments/pricing.html')

@login_required
def create_checkout_session(request):
    """Create Stripe checkout session and redirect to Stripe"""
    if request.method == 'POST':
        try:
            # Get user email, provide fallback if empty
            user_email = request.user.email
            if not user_email or user_email == '':
                user_email = None  # Let Stripe ask for email
            
            # Create Stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        # REPLACE THIS WITH YOUR ACTUAL PRICE ID FROM STRIPE
                        'price': 'price_1TLy60AWobuuao06fKFUGUOx',
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=request.build_absolute_uri(reverse('payment_success')),
                cancel_url=request.build_absolute_uri(reverse('pricing')),
                customer_email=user_email,  # Will be None if no email
            )
            
            # Redirect to Stripe checkout page
            return redirect(checkout_session.url, code=303)
            
        except stripe.error.StripeError as e:
            # Handle Stripe-specific errors
            return render(request, 'payments/error.html', {'error': str(e)})
        except Exception as e:
            # Handle all other errors
            return render(request, 'payments/error.html', {'error': str(e)})
    
    # If not POST request, redirect to pricing page
    return redirect('pricing')

@login_required
def payment_success(request):
    """Display payment success page"""
    return render(request, 'payments/success.html')