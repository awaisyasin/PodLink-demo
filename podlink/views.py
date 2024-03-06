from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404

from accounts.models import CustomUser, GuestProfile, HostProfile

# Create your views here.

def home_view(request):
    return render(request, 'podlink/home.html')


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'podlink/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        user_pk = self.kwargs.get('pk')
        user = get_object_or_404(CustomUser, pk=user_pk)
        try:
            profile = GuestProfile.objects.get(customuser_ptr=user)
        except GuestProfile.DoesNotExist:
            try:
                profile = HostProfile.objects.get(customuser_ptr=user)
            except HostProfile.DoesNotExist:
                raise Http404('User profile not found')
        return profile