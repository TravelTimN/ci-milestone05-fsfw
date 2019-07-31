from django.conf import settings
from django.conf.urls import url, include, handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from accounts import urls as accounts_urls
from accounts.views import index, superuser
from stats import urls as stats_urls
from tickets import urls as tickets_urls
from main.views import handler404, handler500

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^admin/", superuser, name="superuser"),
    url(r"^$", index, name="index"),
    url(r"^accounts/", include(accounts_urls)),
    url(r"^statistics/", include(stats_urls)),
    url(r"^tickets/", include(tickets_urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
else:
    handler404 = "main.views.handler404"
    handler500 = "main.views.handler500"
