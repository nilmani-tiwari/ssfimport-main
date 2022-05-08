from django.contrib import admin
from ssf.models import project_image
from ssf.models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.   VideoSubCategory

@admin.register(project_image)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'slug','desc']
    search_fields = ['title', 'slug']

@admin.register(project_details)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','logo_image','active')


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_image','hit_count')

@admin.register(VideoCategory)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']
    search_fields = ['category_name']

@admin.register(VideoSubCategory)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['subcategory_id', 'subcategory_name']
    search_fields = ['subcategory_name']

@admin.register(VideoUpload)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['video_id','vendor_id', 'title','hit_count', 'video', 'active',"home_active"]
    search_fields = ['title', 'desc','keywords']
    list_filter = ['video_cat', 'sub_cat','active','home_active','created_at','hit_count_generic']

    

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']

@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'subscription_type', 'subscribed', 'created_at', 'modified_at']
    list_filter = ['subscription_type', 'subscribed','created_at']
    search_fields = ['user', 'subscription_type','subscribed','created_at']
    #TODO:  actions = [Subscribe, Unsubscribe]


@admin.register(UserFavoriteVideo)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'label','content_type',"content_id","fab","subscribed"]
    list_filter = ['subscriber', 'label','content_type',"fab","subscribed",'created_at']
    search_fields = ['subscriber', 'label','content_type','created_at']




@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    list_display = ['subscriber','content_type']
    list_filter = ['subscriber','content_type','created_at']
    search_fields = ['subscriber','content_type','created_at']



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','image_url','active']
    search_fields  = ['user','email','active','created_at']
    list_filter = ['active','created_at']


# @admin.register(VideoBlogSubscription)
# class VideoBlogSubscriptionAdmin(admin.ModelAdmin):
#     list_display = ['user', 'subscription_type', 'subscribed', 'created_at', 'modified_at']
#     list_filter = ['subscription_type', 'subscribed','created_at']
#     search_fields = ['user', 'subscription_type','subscribed','created_at']
    #TODO:  actions = [Subscribe, Unsubscribe]

#local project
#testing pull on server
#trying to pull

