"""ssfimport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ssfimport.views import PlanView
from ssftemp.views import homepage ,login_user,about_us,blog,categories,base,contact_us,profile,register_user,forgot_password,submit_post,subscribe_plan
from django.urls import include, path
from paypal_payment.views import *
from ssftemp.views import  *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile, name="profile"),
    path('myprofile/', myprofile, name="myprofile"),
    path('login_user/', login_user,name="login_user"),
    path('logout/', logoutUser, name="logout"),
    path('register_user/', register_user,name="register_user"),
    path('forgot_password/', forgot_password,name="forgot_password"),
    path('subscribe_plan/', subscribe_plan,name="subscribe_plan"),
    path('submit_post/', submit_post,name="submit_post"),
    path('upload/', upload_video,name="upload_video"),
    path('accounts/', include('allauth.urls')),
    path('base/', base.as_view(),name="base"),
     path('categories/', categories,name="categories"),
    path('videos/<slug:slug>/', all_view,name="all_view"),
    path('videos/<slug:slug>/<slug:sub_slug>/', all_view,name="all_view"),
     path('blog/', blog,name="blog"),
      path('blog/<slug:slug>/', single_blog,name="single_blog"),
    path('about_us/', about_us,name="about"),
    path('online_course/', about_course,name="online_course"),
     path('contact_us/', contact_us,name="contact_us"),
     path("subs/", subs, name='subs'),


    path('process_payment/', process_payment, name='process_payment'),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),

     path('checkout/<int:pk>/', checkout, name="checkout"),  
     path('checkout/<int:pk>/<int:video_id>/', checkout, name="checkout"),                    #
     path('complete/', paymentComplete, name="complete"),
     path('upload_data/',upload_data,name='upload_data'),

    path('', include('ssftemp.urls')),

    path('plan/csv/<plan_id>', PlanView.as_view()),



    
    # path('', homepage),
    

    
   
    
   

    path('', include('posts.urls')),
    path('ssf/', include('ssf.urls')),

     path('', include('paypal_payment.urls')),
    
    # path('', include('cart.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)     
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'paypal_payment.views.error_404'
handler500 = 'paypal_payment.views.error_500'
handler403 = 'paypal_payment.views.error_403'
handler400 = 'paypal_payment.views.error_400'

