from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from tickets.models import Ticket
from tickets.forms import TicketForm


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
    ticket.views += 1
    ticket.save()
    context = {
        "ticket": ticket,
    }
    return render(request, "tickets_view_one.html", context)


@login_required
def tickets_edit(request, pk):
    """ Edit a Single Ticket """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
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
