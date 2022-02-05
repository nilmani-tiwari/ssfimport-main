from django.contrib import admin

# Register your models here.

from paypal_payment.models import *
# Register your models here.   VideoSubCategory

@admin.register(Plan)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['plan_id', 'title', 'price', 'slug']
    search_fields = ['title', 'slug']


@admin.register(PlanSubscribedUser)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['subscribed_id', 'plan','email', 'username','amount', 'active','subscribed_date','expiry_date']
    search_fields = ['amount', 'email','amount','username']


@admin.register(ViewPlan)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['view_id', 'video','email', 'username','amount', 'active','subscribed_date','expiry_date']
    search_fields = ['amount', 'email','amount','username']


@admin.register(s3control)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['s3_id', 'active']
    