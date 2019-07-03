from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from accounts import urls as accounts_urls
from accounts.views import index, superuser

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^admin/", superuser, name="superuser"),
    url(r"^$", index, name="index"),
    url(r"^accounts/", include(accounts_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
