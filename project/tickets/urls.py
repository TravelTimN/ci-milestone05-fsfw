from django.urls import path
from tickets.views import (
    tickets_new_bug, tickets_new_feature, tickets_view_one,
    tickets_view_all, tickets_edit, tickets_delete,
    upvote_add, upvote_remove, admin_ticket_status)


urlpatterns = [
    path("", tickets_view_all, name="tickets_view_all"),
    path("bug/new", tickets_new_bug, name="tickets_new_bug"),
    path("feature/new", tickets_new_feature, name="tickets_new_feature"),
    path("<int:pk>", tickets_view_one, name="tickets_view_one"),
    path("edit/<int:pk>", tickets_edit, name="tickets_edit"),
    path("delete/<int:pk>", tickets_delete, name="tickets_delete"),
    path("upvote/add/<int:pk>", upvote_add, name="upvote_add"),
    path("upvote/remove/<int:pk>", upvote_remove, name="upvote_remove"),
    path("admin/edit-status/<int:pk>",
        admin_ticket_status,
        name="admin_ticket_status"),
]
