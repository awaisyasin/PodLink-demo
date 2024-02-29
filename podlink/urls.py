from django.urls import path

from . import views

app_name = 'podlink'

urlpatterns = [
    path('', views.home_view, name='home'),
]
