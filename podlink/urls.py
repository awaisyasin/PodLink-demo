from django.urls import path

from . import views

app_name = 'podlink'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('explore_guests/', views.GuestListView.as_view(), name='guest_list'),
    path('explore_host/', views.HostListView.as_view(), name='host_list'),
]
