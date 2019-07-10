from django.conf.urls import url
from tickets.views import (
    tickets_new_bug, tickets_new_feature, tickets_view_one,
    tickets_view_all, tickets_edit, tickets_delete)


urlpatterns = [
    url(r"^$", tickets_view_all, name="tickets_view_all"),
    url(r"^new/bug$", tickets_new_bug, name="tickets_new_bug"),
    url(r"^new/feature$", tickets_new_feature, name="tickets_new_feature"),
    url(r"^(?P<pk>\d+)$", tickets_view_one, name="tickets_view_one"),
    url(r"^edit/(?P<pk>\d+)$", tickets_edit, name="tickets_edit"),
    url(r"^delete/(?P<pk>\d+)$", tickets_delete, name="tickets_delete"),
]
