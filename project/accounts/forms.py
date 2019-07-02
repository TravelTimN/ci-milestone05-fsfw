from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models import Profile


class UserLoginForm(forms.Form):
    """ Form to log in """
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """ Form to register new users """
    username = forms.CharField(
        label="Username",
        min_length=5,
        max_length=15,
        widget=forms.TextInput(attrs={"autocomplete": "new-password"}),
        required=True)
    email = forms.CharField(
        label="Email Address",
        min_length=5,
        max_length=75,
        widget=forms.EmailInput(attrs={"autocomplete": "new-password"}),
        required=True)
    first_name = forms.CharField(
        label="First Name",
        min_length=2,
        max_length=40,
        widget=forms.TextInput(attrs={"autocomplete": "new-password"}),
        required=True)
    last_name = forms.CharField(
        label="Last Name",
        min_length=2,
        max_length=40,
        widget=forms.TextInput(attrs={"autocomplete": "new-password"}),
        required=True)
    password1 = forms.CharField(
        label="Password",
        min_length=5,
        max_length=20,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=True)
    password2 = forms.CharField(
        label="Repeat Password",
        min_length=5,
        max_length=20,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(
            email=email).exclude(username=username):
            raise forms.ValidationError("Email address must be unique")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password!")
        if password1 != password2:
            raise forms.ValidationError("Passwords must match!")
        return password2


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        min_length=5,
        max_length=15,
        widget=forms.TextInput(attrs={"autocomplete": "new-password"}),
        required=False)
    email = forms.CharField(
        label="Email Address",
        min_length=5,
        max_length=75,
        widget=forms.EmailInput(attrs={"autocomplete": "new-password"}),
        required=False)
    first_name = forms.CharField(
        label="First Name",
        min_length=2,
        max_length=40,
        widget=forms.TextInput(attrs={"autocomplete": "new-password"}),
        required=False)
    last_name = forms.CharField(
        label="Last Name",
        min_length=2,
        max_length=40,
        widget=forms.TextInput(attrs={"autocomplete": "new-password"}),
        required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
