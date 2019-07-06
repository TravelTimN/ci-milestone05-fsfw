from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from tickets.models import Ticket
from tickets.forms import TicketForm


def tickets_view_all(request, sort=None):
    if sort == "bugs":
        tickets = Ticket.objects.filter(ticket_type="Bug")
    elif sort == "features":
        tickets = Ticket.objects.filter(ticket_type="Feature")
    else:
        tickets = Ticket.objects.all()
    context = {
        "tickets": tickets,
    }
    return render(request, "tickets_all.html", context)


def tickets_view_one(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    views += 1
    context = {
        "ticket": ticket,
    }
    return render(request, "tickets_one.html", context)


@login_required
def tickets_edit_one(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method=="POST":
        form = TicketForm(
            request.POST,
            request.FILES,
            instance=ticket)
        if form.is_valid():
            ticket.title = form.cleaned_data["title"]
            ticket.description = form.cleaned_data["description"]
            ticket.save()
            return redirect(tickets_view_one, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
        template_name = (
            "tickets_edit_bug.html" if ticket.ticket_type == "Bug" else \
                "tickest_edit_feature.html")
    context = {
        "form": form,
    }
    return render(request, template_name, context)


@login_required
def tickets_delete_one(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    return redirect(reverse("tickets_view_all"))


@login_required
def tickets_new_bug(request):
    if request.method=="POST":
        form = TicketForm(
            request.POST,
            request.FILES)
        if form.is_valid():
            ticket = Ticket(
                author = request.user,
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                ticket_type = "Bug",
                date_created = timezone.now())
            ticket.save()
            return redirect(tickets_view_one, ticket.pk)
    else:
        form = TicketForm()
    context = {
        "form": form,
    }
    return render(request, "tickets_new_bug.html", context)
