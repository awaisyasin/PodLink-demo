from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('guestsignup/', views.guest_signup_view, name='guest_signup'),
    path('hostsignup/', views.host_signup_view, name='host_signup'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('verify-email/<str:token>/', views.email_verify_view, name='email_verify'),
    path('logout/', views.logout_view, name='logout'),
]
