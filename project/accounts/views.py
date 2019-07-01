from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


def superuser(request):
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
                    request, "You have been successfully logged in!")
                return redirect(reverse("profile"))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect.")
    else:
        login_form = UserLoginForm()

    return render(request, "login.html", {"login_form": login_form})


@login_required
def logout(request):
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect(reverse("index"))


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
                messages.success(request, "You have successfully registered!")
                return redirect(reverse("profile"))
            else:
                messages.error(
                    request, "There has been an error with registration, please try again!")
    else:
        register_form = UserRegistrationForm()

    return render(request, "register.html", {
        "register_form": register_form})


def profile(request):
    """ The user's profile page """
    user = User.objects.get(email=request.user.email)
    return render(request, "profile.html", {"profile": user})
