from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from accounts import urls as accounts_urls
from accounts.views import index, superuser
from tickets import urls as tickets_urls

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^admin/", superuser, name="superuser"),
    url(r"^$", index, name="index"),
    url(r"^accounts/", include(accounts_urls)),
    url(r"^tickets/", include(tickets_urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
