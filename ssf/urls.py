from django.contrib import admin
from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include
from ssf.views import BaseDetailView,base2,BlogListView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('posts/', PostListView.as_view(), name='posts'),   # BlogListView
    path('base1/', BlogListView.as_view(), name='base1'),
    path('base1/<slug:slug>/', BaseDetailView.as_view(), name='base1'),
    path('base2/', base2 , name='base2'),
    path('hitcount_project/', include(('hitcount.urls', 'hitcount_project'), namespace='hitcount_project')),
]