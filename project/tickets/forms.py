import calendar
from datetime import datetime
from django import forms
from tickets.models import Ticket, Comment


# ----- TICKETS ----- #
class TicketForm(forms.ModelForm):
    """ Form to allow User to submit new Ticket """
    title = forms.CharField(
        label="Title of Ticket",
        min_length=5,
        max_length=75,
        widget=forms.TextInput(),
        required=True)
    description = forms.CharField(
        label="Ticket Details",
        min_length=20,
        max_length=2000,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Ticket
        fields = ["title", "description"]


class DonationForm(forms.Form):
    donation_amount = forms.IntegerField(
        label="Donation Amount",
        widget=forms.NumberInput(
            attrs={
                "type":"range", "step":"5", "value":"10",
                "min":"5", "max":"100"}),
        required=False)


# ----- COMMENTS ----- #
class CommentForm(forms.ModelForm):
    """ Form to allow Users to add Comments on Tickets """
    comment = forms.CharField(
        label="Your Comment",
        min_length=5,
        max_length=2000,
        widget=forms.Textarea(),
        required=True)

    class Meta:
        model = Comment
        fields = ["comment"]
