from django.db import models
from django.conf import settings
from django.utils import timezone


class Ticket(models.Model):
    """
    Allow users to open tickets (bugs or features).
    Default status should be 'open' with current timestamp.
    """
    TICKET_TYPE_CHOICES = [
        ("Bug", "Bug"),
        ("Feature", "Feature")
    ]
    TICKET_STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Closed", "Closed"),
    ]

    # ticket fields (non-editable)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        on_delete=models.CASCADE)
    author = models.CharField(
        max_length=25,
        blank=False)
    status = models.CharField(
        max_length=11,
        default="Open",
        choices=TICKET_STATUS_CHOICES)
    ticket_type = models.CharField(
        max_length=7,
        default="Bug",
        choices=TICKET_TYPE_CHOICES)
    date_created = models.DateTimeField(
        blank=False,
        null=False,
        default=timezone.now)
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
        decimal_places=2)

    # user fields (editable)
    title = models.CharField(
        max_length=75,
        default="",
        blank=False,
        help_text="Titles can have a maximum of 75 characters.")
    description = models.TextField(
        max_length=2000,
        default="",
        blank=False,
        help_text="Descriptions can have a maximum of 2,000 characters.")

    def __str__(self):
        return f"#{0} [{1}] - {2}".format(self.id, self.type, self.title)

    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)
        self.author = self.user.author
