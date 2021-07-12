from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stutor.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .forms import create_tutor_form

@unauthenticated_user
def tutor_register_page(request):

    form = create_tutor_form()
    if request.method == 'POST':
        form = create_tutor_form(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            username = form.cleaned_data.get('username')

            user_group = Group.objects.get(name="tutor")
            user.groups.add(user_group)
            tutor_account.objects.create(
                user=user,
                name=user.username,
            )


            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'tutor/registerpage.html', context)

@unauthenticated_user
def student_login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,  password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'tutor/loginpage.html', context)

def logout_user(request):
    logout(request)
    return redirect('tutor_login')

def home(request):
    return render(request, 'tutor/home.html')

def settings(request):
    return render(request, 'tutor/settings.html')