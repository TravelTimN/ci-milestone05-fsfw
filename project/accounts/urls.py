from django.conf.urls import url, include
from accounts import urls_reset
from accounts.views import login, logout, profile, register


urlpatterns = [
    url(r"^login/$", login, name="login"),
    url(r"^logout/$", logout, name="logout"),
    url(r"^profile/$", profile, name="profile"),
    url(r"^register/$", register, name="register"),
    url(r"^password-reset/", include(urls_reset))
]
