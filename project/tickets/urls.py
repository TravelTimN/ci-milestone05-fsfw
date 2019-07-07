from django.conf.urls import url
from tickets.views import (
    tickets_view_all, tickets_new_bug)


urlpatterns = [
    url(r"^$", tickets_view_all, name="tickets_view_all"),
    url(r"^new/bug$", tickets_new_bug, name="tickets_new_bug"),
]
