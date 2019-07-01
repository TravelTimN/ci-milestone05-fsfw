from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_urls
from accounts.views import index, superuser

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^admin/", superuser, name="superuser"),
    url(r"^$", index, name="index"),
    url(r"^accounts/", include(accounts_urls)),
]
