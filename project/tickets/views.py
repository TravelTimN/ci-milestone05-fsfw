from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from tickets.models import Ticket
from tickets.forms import TicketForm


def tickets_view_all(request):
    tickets = Ticket.objects.filter(
        date_created__lte=timezone.now()
    ).order_by("-date_created")
    context = {
        "tickets": tickets,
    }
    return render(request, "tickets_view_all.html", context)


@login_required
def tickets_new_bug(request):
    if request.method=="POST":
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.instance.author = request.user
            ticket_form.save()
            messages.success(
                request, f"Ticket successfully created for your Bug!")
            return redirect(tickets_view_all)
    else:
        ticket_form = TicketForm()
    context = {
        "ticket_form": ticket_form,
    }
    return render(request, "tickets_new_bug.html", context)


def tickets_view_one(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    context = {
        "ticket": ticket,
    }
    return render(request, "tickets_view_one.html", context)


@login_required
def tickets_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, instance=ticket)
        if ticket_form.is_valid():
            ticket_form.instance.author = request.user
            ticket_form.instance.date_edited = timezone.now()
            ticket_form.save()
            messages.success(
                request, f"Ticket successfully updated!")
            return redirect(tickets_view_one, ticket.pk)
    else:
        ticket_form = TicketForm(instance=ticket)
    template_name = (
        "tickets_edit_bug.html" if ticket.ticket_type == "Bug" else \
            "tickets_edit_feature.html"
    )
    context = {
        "ticket_form": ticket_form,
    }
    return render(request, template_name, context)
