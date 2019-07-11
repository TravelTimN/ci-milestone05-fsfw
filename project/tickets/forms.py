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
