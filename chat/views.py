from django.shortcuts import render

# Create your views here.

def chat_view(request):
    return render(request, 'chat/chat.html')


def room_view(request, other_user_id):
    current_user_id = request.user.id
    return render(request, 'chat/room.html', {'current_user_id': current_user_id, 'other_user_id': other_user_id})