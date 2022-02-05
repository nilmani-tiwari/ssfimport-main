from django.contrib import admin
from django.urls import path
from . import views

# from django.contrib import admin
# from django.urls import path, include
# from posts.views import PostListView, PostDetailView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('posts/', PostListView.as_view(), name='posts'),
    # path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
]