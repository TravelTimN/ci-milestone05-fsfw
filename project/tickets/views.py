from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from tickets.models import Ticket, Comment
from tickets.forms import TicketForm, CommentForm


def tickets_view_all(request):
    """ View ALL Tickets """
    tickets = Ticket.objects.filter(
        date_created__lte=timezone.now()
    ).order_by("-date_created")
    context = {
        "tickets": tickets,
    }
    return render(request, "tickets_view_all.html", context)


@login_required
def tickets_new_bug(request):
    """ Create a NEW Ticket (Bug) """
    if request.method=="POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.instance.author = request.user
            ticket_form.instance.ticket_type = "Bug"
            new_ticket = ticket_form.save()
            new_ticket_id = new_ticket.pk
            messages.success(
                request, f"SUCCESS! Ticket for a BUG created!")
            return redirect(tickets_view_one, new_ticket_id)
    else:
        ticket_form = TicketForm()
    context = {
        "ticket_form": ticket_form,
    }
    return render(request, "tickets_new_bug.html", context)


@login_required
def tickets_new_feature(request):
    """ Create a NEW Ticket (Feature) """
    if request.method=="POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.instance.author = request.user
            ticket_form.instance.ticket_type = "Feature"
            new_ticket = ticket_form.save()
            new_ticket_id = new_ticket.pk
            messages.success(
                request, f"SUCCESS! Ticket for a FEATURE created!")
            return redirect(tickets_view_one, new_ticket_id)
    else:
        ticket_form = TicketForm()
    context = {
        "ticket_form": ticket_form,
    }
    return render(request, "tickets_new_feature.html", context)


def tickets_view_one(request, pk):
    """ View a Single Ticket """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    # allow users to add Comments
    if request.method=="POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.commenter = request.user
            comment_form.instance.ticket = ticket
            comment_form.save()
            ticket.views -= 1
            ticket.save()
            messages.success(
                request, f"Your comment was added!")
            return redirect(tickets_view_one, ticket.pk)
    else:
        comment_form = CommentForm()
    ticket.views += 1
    ticket.save()
    comments = Comment.objects.filter(ticket_id=ticket.pk)
    context = {
        "comment_form": comment_form,
        "comments": comments,
        "ticket": ticket,
    }
    return render(request, "tickets_view_one.html", context)


@login_required
def tickets_edit(request, pk):
    """ Edit a Single Ticket """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method=="POST":
        ticket_form = TicketForm(request.POST, instance=ticket)
        if ticket_form.is_valid():
            ticket_form.instance.date_edited = timezone.now()
            ticket_form.save()
            messages.success(
                request, f"Ticket successfully updated!")
            return redirect(tickets_view_one, ticket.pk)
    else:
        ticket_form = TicketForm(instance=ticket)
    context = {
        "ticket": ticket,
        "ticket_form": ticket_form,
    }
    return render(request, "tickets_edit.html", context)


@login_required
def tickets_delete(request, pk):
    """ Delete a Ticket """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    ticket.delete()
    messages.success(
        request, f"Your ticket has been deleted!")
    return redirect(tickets_view_all)
