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
    gross_total = forms.IntegerField(
        label="Donation Amount",
        widget=forms.NumberInput(
            attrs={
                "type":"range", "step":"5", "value":"50",
                "min":"10", "max":"100"}),
        required=True)

    class Meta:
        model = Ticket
        fields = ["title", "description"]


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


# ----- PAYMENTS ----- #
class PaymentForm(forms.Form):
    """ Form to allow users to pay for Feature payments """
    month_choices = [(m, calendar.month_name[m]) for m in range(1, 13)]
    year_choices = [(y, y) for y in range(
        datetime.now().year, datetime.now().year + 16)]

    credit_card_number = forms.CharField(
        label="Credit Card Number",
        required=False)
    cvv = forms.CharField(
        label="Security Code (CVV)",
        required=False)
    expiry_month = forms.ChoiceField(
        label="Expiry Month",
        choices=month_choices,
        required=False)
    expiry_year = forms.ChoiceField(
        label="Expiry Year",
        choices=year_choices,
        required=False)
    stripe_id = forms.CharField(
        widget=forms.HiddenInput)
