from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ----- TICKET TYPE ----- #
class TicketType(models.Model):
    TICKET_TYPE_CHOICES = (
        ("Bug", "Bug"),
        ("Feature", "Feature")
    )
    ticket_type = models.CharField(
        max_length=7,
        unique=True,
        choices=TICKET_TYPE_CHOICES)

    class Meta:
        verbose_name = ("Ticket Type")
        verbose_name_plural = ("Ticket Types")

    def __str__(self):
        return self.ticket_type


# ----- TICKET STATUS ----- #
class TicketStatus(models.Model):
    TICKET_STATUS_CHOICES = (
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Closed", "Closed"),
    )
    ticket_status = models.CharField(
        max_length=11,
        unique=True,
        choices=TICKET_STATUS_CHOICES)

    class Meta:
        verbose_name = ("Ticket Status")
        verbose_name_plural = ("Ticket Status")

    def __str__(self):
        return self.ticket_status


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
    ticket_status = models.ForeignKey(
        TicketStatus,
        null=True,
        on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(
        TicketType,
        null=True,
        on_delete=models.CASCADE)
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
    total_donations = models.IntegerField(
        default=0)

    class Meta:
        ordering = ("-date_edited", )

    def __str__(self):
        return "#{0} [{1}] - {2}".format(
            self.id, self.ticket_type, self.title)


# ----- COMMENTS ----- #
class Comment(models.Model):
    """ Allow users to add Comments onto Tickets (Bugs or Features). """
    # user fields (editable)
    comment = models.TextField(
        max_length=2000,
        null=True)

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


# ----- UPVOTES ----- #
class Upvote(models.Model):
    """ Allow users to Upvote a Ticket (Bugs or Features) """
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    ticket = models.ForeignKey(
        Ticket,
        null=True,
        on_delete=models.CASCADE)

    def __str__(self):
        return "Upvote by {0} on Ticket {1}".format(
            self.user.username, self.ticket.id)
