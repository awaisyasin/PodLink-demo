from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_view, name='chat'),
    # path('<str:room_name>/', views.room_view, name='room'),
    path('<int:other_user_id>/', views.room_view, name='room'),
]
