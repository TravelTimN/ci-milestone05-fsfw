from django.contrib import admin
from tickets.models import Ticket, Comment, Upvote


admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Upvote)
