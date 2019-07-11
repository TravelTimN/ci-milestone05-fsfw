from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import (
    UserLoginForm, UserRegistrationForm,
    UserUpdateForm, ProfileUpdateForm)


def superuser(request):
    """ Superuser = Admin only access """
    if request.user.is_superuser:
        return redirect(reverse("superuser"))


def index(request):
    """ Return the index.html file """
    return render(request, "index.html")


def login(request):
    """ Logs the user into the app """
    if request.user.is_authenticated:
        return redirect(reverse("index"))
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST["username"],
                password=request.POST["password"])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request, f"Welcome back, {user.first_name}!")
                return redirect(reverse("profile"))
            else:
                messages.error(
                    request, f"Username or Password is incorrect.")
    else:
        login_form = UserLoginForm()
    context = {
        "login_form": login_form,
    }
    return render(request, "login.html", context)


@login_required
def logout(request):
    """ Log the user out """
    messages.success(request, f"Hope to see you again soon!")
    auth.logout(request)
    return redirect(reverse("login"))


def register(request):
    """ Renders the registration page """
    if request.user.is_authenticated:
            return redirect(reverse("profile"))
    if request.method=="POST":
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = auth.authenticate(
                username=request.POST["username"],
                password=request.POST["password1"])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, f"Welcome, {user.first_name}!")
                return redirect(reverse("profile"))
            else:
                messages.error(
                    request, f"Error with registration. Please try again!")
    else:
        register_form = UserRegistrationForm()
    context = {
        "register_form": register_form,
    }
    return render(request, "register.html", context)


@login_required
def profile(request):
    """ The user's profile page """
    user = User.objects.get(email=request.user.email)
    if request.method=="POST":
        update_form = UserUpdateForm(
            request.POST,
            instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(
                request, f"Profile successfully updated!")
            return redirect(reverse("profile"))
    else:
        update_form = UserUpdateForm(
            instance=request.user)
        profile_form = ProfileUpdateForm(
            instance=request.user.profile)
    context = {
        "update_form": update_form,
        "profile_form": profile_form,
        "profile": user
    }
    return render(request, "profile.html", context)
