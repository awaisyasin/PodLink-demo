from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

from . import forms

# Create your views here.

def guest_signup_view(request):
    if request.method == 'POST':
        pass
    else:
        form = forms.GuestSignUpForm
    return render(request, 'accounts/guest_signup_form.html', {'form': form})

def host_signup_view(request):
    if request.method == 'POST':
        pass
    else:
        form = forms.HostSignUpForm
    return render(request, 'accounts/host_signup_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})