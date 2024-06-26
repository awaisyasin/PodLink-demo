from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

import uuid

from . import forms
from . import models

# Create your views here.

def signup_view(request):
    return render(request, 'accounts/signup.html')


def guest_signup_view(request):
    if request.method == 'POST':
        form = forms.GuestSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            token = str(uuid.uuid4())
            user.email_verification_token = token

            subject = 'Verify your email address'
            current_site = get_current_site(request)
            verification_link = f'http://{current_site}/verify-email/{token}/'
            message = f'Click the following link to verify your email:\n{verification_link}'
            from_email = 'no-reply@podlink.com'
            recipient_list = [form.cleaned_data['email'],]
            send_mail(subject, message, from_email, recipient_list)
            user.save()
            return redirect('accounts:login')
    else:
        form = forms.GuestSignUpForm()
    return render(request, 'accounts/guest_signup_form.html', {'form': form})


def host_signup_view(request):
    if request.method == 'POST':
        form = forms.HostSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            token = str(uuid.uuid4())
            user.email_verification_token = token

            subject = 'Verify your email address'
            current_site = get_current_site(request)
            verification_link = f'http://{current_site}/verify-email/{token}/'
            message = f'Click the following link to verify your email:\n{verification_link}'
            from_email = 'no-reply@podlink.com'
            recipient_list = [form.cleaned_data['email'],]
            send_mail(subject, message, from_email, recipient_list)
            user.save()
            return redirect('accounts:login')
    else:
        form = forms.HostSignUpForm()
    return render(request, 'accounts/host_signup_form.html', {'form': form})


def email_verify_view(requet, token):
    user = get_object_or_404(models.CustomUser, email_verification_token=token)
    if user:
        user.is_email_verified = True
        user.email_verification_token = None
        user.save()
        return redirect('accounts:login')


def login_view(request):
    if request.method == 'POST':
        form = forms.CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_email_verified:
                    login(request, user)
                    return redirect('podlink:home')
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')