from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from tickets.models import Ticket, Comment, Upvote
from tickets.forms import TicketForm, CommentForm, PaymentForm
import stripe


stripe.api_key = settings.STRIPE_SECRET


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
        payment_form = PaymentForm(request.POST)
        if ticket_form.is_valid() and payment_form.is_valid():
            # amount to pay / donate
            gross_total = 0
            gross_total += int(request.POST.get("gross_total"))
            try:
                # build Stripe payment
                customer = stripe.Charge.create(
                    amount = int(gross_total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data["stripe_id"],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if customer.paid:
                ticket_form.instance.author = request.user
                ticket_form.instance.ticket_type = "Feature"
                ticket_form.instance.gross_total = gross_total
                new_ticket = ticket_form.save()
                new_ticket_id = new_ticket.pk
                messages.success(
                    request, f"SUCCESS! Ticket for a FEATURE created!\
                        €{gross_total} was charged to your card.")
                return redirect(tickets_view_one, new_ticket_id)
            else:
                messages.error(request, "Unable to take payment!")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        ticket_form = TicketForm()
        payment_form = PaymentForm()
    context = {
        "ticket_form": ticket_form,
        "payment_form": payment_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }
    return render(request, "tickets_new_feature.html", context)


def tickets_view_one(request, pk):
    """ View a Single Ticket """
    # get ticket details
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    # increase number of views by 1
    ticket.views += 1
    ticket.save()
    # filter comments on specific ticket
    comments = Comment.objects.filter(ticket_id=ticket.pk)
    # filter upvotes on specific ticket by user ID
    upvotes = Upvote.objects.filter(ticket_id=ticket.pk).values("user_id")
    voters = [vote["user_id"] for vote in upvotes]
    # POST methods
    if request.method=="POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.commenter = request.user
            comment_form.instance.ticket = ticket
            comment_form.save()
            # remove two ticket views to avoid duplicates on POST
            ticket.views -= 2
            ticket.save()
            messages.success(
                request, f"Your comment was added!")
            return redirect(tickets_view_one, ticket.pk)
    else:
        comment_form = CommentForm()
    context = {
        "comment_form": comment_form,
        "comments": comments,
        "ticket": ticket,
        "voters": voters,
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


@login_required
def upvote_add(request, pk):
    """ Upvote a Ticket """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    # remove a ticket view to avoid duplicates
    ticket.views -= 1
    ticket.save()
    Upvote.objects.create(
        ticket_id=ticket.pk,
        user_id=request.user.id)
    messages.success(
        request, f"Thanks for your vote!")
    return redirect(tickets_view_one, ticket.pk)


@login_required
def upvote_remove(request, pk):
    """ Remove Upvote from a Ticket """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes -= 1
    # remove a ticket view to avoid duplicates
    ticket.views -= 1
    ticket.save()
    Upvote.objects.filter(
        ticket_id=ticket.pk,
        user_id=request.user.id).delete()
    messages.success(
        request, f"Your vote has been removed.")
    return redirect(tickets_view_one, ticket.pk)
