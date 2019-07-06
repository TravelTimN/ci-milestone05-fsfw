from django.conf.urls import url
from tickets.views import (
    tickets_view_all, tickets_view_one,
    tickets_new_bug, tickets_edit_one,
    tickets_delete_one)


app_name = "tickets"


urlpatterns = [
    url(r"^$", tickets_view_all, name="tickets_view_all"),
    url(r"^(?P<sort>\w+)/$", tickets_view_all, name="sort"),
    url(r"^(?P<pk>\d+)/$", tickets_view_one, name="tickets_view_one"),
    url(r"^new/bug$", tickets_new_bug, name="tickets_new_bug"),
    url(r"^edit/(?P<pk>\d+)$", tickets_edit_one, name="tickets_edit_one"),
    url(r"^delete/(?P<pk>\d+)$", tickets_delete_one, name="tickets_delete_one"),
]
