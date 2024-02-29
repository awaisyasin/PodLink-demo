from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('guestsignup/', views.guest_signup_view, name='guest_signup'),
    path('hostsignup/', views.host_signup_view, name='host_signup'),
]
