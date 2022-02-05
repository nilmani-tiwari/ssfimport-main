from django.contrib import admin
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include
# from posts.views import PostListView, PostDetailView
from django.contrib.auth.decorators import login_required
from ssftemp.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', homepage.as_view(), name='homepage'),
    # path('<slug:slug>/', login_required(single_video.as_view(),login_url='/admin/login/?next=/admin/'), name='single_video'),
    path('<slug:slug>/', login_required(single_video.as_view(),login_url='/login_user/'), name='single_video'),

    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]