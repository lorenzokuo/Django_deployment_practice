from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    if 'first_name' not in request.session:
        return render(request, 'login_app/index.html')
    else:
        return render(request, 'user_app/home.html')

def register(request):
    if User.UserManager.valid_registration(request.POST, request):
        valid = True
        user = User.objects.get(email = request.POST['email_address'])
        request.session['first_name'] = user.first_name
        request.session['user_id'] = user.id
        return redirect(reverse('userspace:home'))
    else:
        valid = False
        return redirect(reverse('loginspace:index'))

def login(request):
    if User.UserManager.exisiting_user(request.POST, request):
        valid = True
        user = User.objects.get(email = request.POST['email_address'])
        request.session['first_name'] = user.first_name
        request.session['email_address'] = user.last_name
        request.session['user_id'] = user.id
        return redirect(reverse('userspace:home'))
    else:
        valid = False
        return redirect(reverse('loginspace:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('loginspace:index'))