from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, UpdateProfileForm, UpdateUserForm

def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You successfully login!")
            return redirect("accounts:profile")
    else:
        form = SignUpForm()
    return render(request, "accounts/registration.html", {"form" : form})

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

@login_required
def update_profile_and_user(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile updated successfully!")
            return redirect("accounts:profile")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, "accounts/profile.html", {"user_form" : user_form, "profile_form" : profile_form})


def custom_logout(request):
    logout(request)
    messages.success(request, "You successfully logout!")
    return redirect("accounts:login")


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # залишає користувача залогіненим
            messages.success(request, "Your password was successfully updated!")
            return redirect("accounts:profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {"form" : form})