from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpform, editprofileform, changepasswordform


def home(request):
    return render(request, 'webapp/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('You are logged in'))
            return redirect('home')
        else:
            messages.success(request, ('Wrong username or Password'))
            return redirect('login')

    else:
        return render(request, 'webapp/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You are logged out'))
    return redirect('home')


def user_details(request):
    return render(request, 'webapp/user_details.html', {})


def Signup_form(request):
    if request.method == 'POST':
        form = SignUpform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered'))
            return redirect('home')
    else:
        form = SignUpform()

    context = {'form': form}
    return render(request, 'webapp/Signup_form.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = editprofileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, (' Profile Updated successfully'))
            return redirect('details')
    else:
        form = editprofileform(instance=request.user)

    context = {'form': form}
    return render(request, 'webapp/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = changepasswordform(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Password changed successfully'))
            return redirect('change_password')
    else:
        form = changepasswordform(user=request.user)

    context = {'form': form}
    return render(request, 'webapp/change_password.html', context)
