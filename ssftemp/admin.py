from django.contrib import admin

# Register your models here.
from ssftemp.models import *


def refresh_video(modeladmin, request, queryset):
    for video in queryset:
        video.refresh()
    return

refresh_video.short_description = "Refresh Video"

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['ssf_id','video','ssf_id', 'title', 'duration']
    search_fields = ['title']
    actions = [refresh_video]


@admin.register(BlogPage)
class BlogPage(admin.ModelAdmin):
    list_display = ['image','slug', 'title', 'content']
    search_fields = ['title']
    #actions = [refresh_video]

def refresh_cat(modeladmin, request, queryset):
    for cat in queryset:
        cat.refresh()
    return

refresh_video.short_description = "Refresh Category"

@admin.register(VideoCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['ssf_id', 'name', 'parent', 'desc']
    list_filter = ['parent']
    actions = [refresh_cat]


def refresh_maps(modeladmin, request, queryset):
    VideoCategoryMapping.populate()
    return

refresh_video.short_description = "Refresh Mappings"

@admin.register(VideoCategoryMapping)
class VideoCategoryMappingAdmin(admin.ModelAdmin):
    list_display = ['video', 'category']
    list_filter = ['category']
    search_fields = ['category__name', 'video__title']
    actions = [refresh_maps]


@admin.register(SubscribedUser)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['ssf_id', 'email', 'username', 'fname']
    search_fields = ['email', 'username']


def generate_csv(modeladmin, request, queryset):
    for plan in queryset:
        plan.generate_csv()
    return


generate_csv.short_description = "Generate CSV"

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'ssf_id', 'price', 'description', 'type']
    list_filter = ['type']
    actions = [generate_csv]


@admin.register(SubscribedUserPlanMapping)
class SubscriberPlanMapAdmin(admin.ModelAdmin):
    list_display = ['ssf_id', 'subscriber', 'plan', 'exp_date']
    search_fields = ['subscribe_username']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['ssf_id', 'video', 'subscriber', 'comment']

@admin.register(UserFavorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'video']
