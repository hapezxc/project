from django.urls import path
from . import views
from .views import update_profile
from .views import contact
from .views import admin_dashboard_view
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('room/', views.room_view, name='room'),
    path('contact/', contact, name='contact'),
    path('update_user/', views.update_user_view, name='update_user'),
    path('booking/', views.booking_view, name='booking'),
    path('user_logout/', views.logout_view, name='user_logout'),
    path('registration/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('basic/', views.basic_view, name='basic'),
    path('update_profile/', update_profile, name='update_user'),
    path('bookings/', views.booking_view, name='bookings'),
    path('checkout_basic/', views.checkout_view, name='checkout_basic'),
    path('admin_dashboard/', views.dashboard_view, name='dashboard'),
    path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),



]
