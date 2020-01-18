from django.urls import include, path
from accounts import urls_reset
from accounts.views import login, logout, profile, register


urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
    path("password-reset/", include(urls_reset))
]
