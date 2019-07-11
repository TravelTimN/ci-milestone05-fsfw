from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# drop-down options for Tickets
TICKET_TYPE_CHOICES = (
    ("Bug", "Bug"),
    ("Feature", "Feature")
)
TICKET_STATUS_CHOICES = (
    ("Open", "Open"),
    ("In Progress", "In Progress"),
    ("Closed", "Closed"),
)


# ----- TICKETS ----- #
class Ticket(models.Model):
    """
    Allow users to open Tickets (Bugs or Features).
    Default status should be 'Open' with current timestamp.
    """
    # user fields (editable)
    title = models.CharField(
        max_length=75,
        default="",
        blank=False)
    description = models.TextField(
        max_length=2000,
        default="",
        blank=False)

    # ticket fields (non-editable)
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    ticket_status = models.CharField(
        max_length=11,
        default="Open",
        null=True,
        choices=TICKET_STATUS_CHOICES)
    ticket_type = models.CharField(
        max_length=7,
        default="Bug",
        null=True,
        choices=TICKET_TYPE_CHOICES)
    date_created = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    date_edited = models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now)
    views = models.IntegerField(
        default=0)
    upvotes = models.IntegerField(
        default=0)
    gross_total = models.DecimalField(
        default=0,
        max_digits=7,
        decimal_places=0)

    def __str__(self):
        return "#{0} [{1}] - {2}".format(
            self.id, self.ticket_type, self.title)


class Comment(models.Model):
    """ Allow users to add Comments onto Tickets (Bugs or Features). """
    # user fields (editable)
    comment = models.TextField(
        max_length=2000,
        null=True,
        help_text="Comments can have a maximum of 2,000 characters.")

    # comment fields (non-editable)
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.CASCADE)
    commenter = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    date_commented = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return "Comment #{0} by {1} on Ticket #{2}".format(
            self.id, self.commenter, self.ticket.id)
