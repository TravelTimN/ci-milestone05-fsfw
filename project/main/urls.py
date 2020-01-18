from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from accounts import urls as accounts_urls
from accounts.views import index, superuser
from stats import urls as stats_urls
from tickets import urls as tickets_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/", superuser, name="superuse"),
    path("", index, name="index"),
    path("accounts/", include(accounts_urls)),
    path("statistics/", include(stats_urls)),
    path("tickets/", include(tickets_urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
