from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, ProfileEditForm, ChangePasswordForm
from .models import UserModel
# from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash


@login_required
def profile_edit(request):
    form = ProfileEditForm(instance=request.user)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'profile_edit.html', context={
        'form' : form
    })


@login_required
def profile_view(request):
    return render(request, 'profile.html', context={

    })

def registration_view(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'registration.html', context={
         'form': form
    })

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            form.add_error("password", "Username and password is incorrect")
    return render(request, 'login.html', context={
           "form": form
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def change_password_view(request):
    form =  ChangePasswordForm()
    user = request.user
    if request.method ==  "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data["password"])
            user.save()
            update_session_auth_hash(request, user)
            return redirect("profile")
    return render(request, "profile_edit.html", context={
     'form': form
    })


def forget_password_view(request):
    pass

    