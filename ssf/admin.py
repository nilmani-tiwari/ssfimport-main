from django.contrib import admin
from ssf.models import project_image
from ssf.models import *
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
    list_display = ['video_id', 'title','hit_count', 'video', 'active',"home_active"]
    search_fields = ['title', 'desc','keywords']
