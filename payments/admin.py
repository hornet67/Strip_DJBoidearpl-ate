from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'stripe_customer_id', 'current_period_end', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['user__email', 'stripe_customer_id']
    readonly_fields = ['created_at', 'updated_at']