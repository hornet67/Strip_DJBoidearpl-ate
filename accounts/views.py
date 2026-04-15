
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from payments.models import UserSubscription

@login_required
def dashboard(request):
    # Get user's subscription status
    is_premium = False
    try:
        sub = UserSubscription.objects.get(user=request.user)
        is_premium = sub.is_active
    except UserSubscription.DoesNotExist:
        is_premium = False
    
    return render(request, 'dashboard.html', {
        'is_premium': is_premium
    })

@login_required
def premium_content(request):
    # Check if user has active subscription
    is_premium = False
    try:
        sub = UserSubscription.objects.get(user=request.user)
        is_premium = sub.is_active
    except UserSubscription.DoesNotExist:
        is_premium = False
    
    if is_premium:
        return render(request, 'premium_content.html')
    return redirect('pricing')