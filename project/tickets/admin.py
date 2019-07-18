from django.contrib import admin
from tickets.models import Ticket, TicketStatus, TicketType, Comment, Upvote


admin.site.register(Ticket)
admin.site.register(TicketStatus)
admin.site.register(TicketType)
admin.site.register(Comment)
admin.site.register(Upvote)
