from django import forms
from tickets.models import Ticket


class TicketForm(forms.ModelForm):
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
        fields = (
            "title",
            "description",
        )
