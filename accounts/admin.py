from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from payments.models import UserSubscription

class UserSubscriptionInline(admin.StackedInline):
    model = UserSubscription
    can_delete = False
    verbose_name_plural = 'Subscription'

class CustomUserAdmin(UserAdmin):
    inlines = [UserSubscriptionInline]

# Re-register User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)