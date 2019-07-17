from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from accounts.models import Profile
from tickets.models import Ticket, Comment, Upvote
from tickets.forms import TicketForm, CommentForm, DonationForm
import stripe


stripe.api_key = settings.STRIPE_SECRET


def tickets_view_all(request):
    """ View ALL Tickets """
    tickets = Ticket.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(tickets, 8)
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)
    # tickets = Ticket.objects.filter(
    #     date_created__lte=timezone.now()
    # ).order_by("-date_created")
    context = {
        "tickets": tickets,
    }
    return render(request, "tickets_view_all.html", context)


@login_required
def tickets_new_bug(request):
    """ Create a NEW Ticket (Bug) """
    if request.method == "POST":
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
    if request.method == "POST":
        ticket_form = TicketForm(request.POST)
        donation_form = DonationForm(request.POST)
        if ticket_form.is_valid() and donation_form.is_valid():
            # amount to pay / donate
            donation_amount = 0
            donation_amount += int(request.POST.get("donation_amount"))
            try:
                # build Stripe payment
                token = request.POST["stripeToken"]
                customer = stripe.Charge.create(
                    amount=int(donation_amount * 100),
                    currency="EUR",
                    description=(
                        request.user.email +
                        " (" + request.user.get_full_name() + ")"),
                    source=token,
                )
            except stripe.error.CardError:
                # Stripe payment error
                messages.error(request, f"Your card was declined!")
            # authorization is valid - payment successful
            if customer.paid:
                ticket_form.instance.author = request.user
                ticket_form.instance.ticket_type = "Feature"
                ticket_form.instance.total_donations = donation_amount
                # update user Profile with additional donation amount
                get_user_donations = Profile.objects.values_list(
                    "total_donated", flat=True).get(user_id=request.user.id)
                new_user_donations = get_user_donations + donation_amount
                Profile.objects.filter(
                    user_id=request.user.id).update(
                        total_donated=new_user_donations)
                # update ticket status to In Progress if €100 goal is achieved
                if donation_amount >= int(100):
                    ticket_form.instance.ticket_status = "In Progress"
                new_ticket = ticket_form.save()
                new_ticket_id = new_ticket.pk
                messages.success(
                    request, f"SUCCESS! Ticket for a FEATURE created!\
                        €{donation_amount} was charged to your card.")
                return redirect(tickets_view_one, new_ticket_id)
            else:
                messages.error(request, f"Unable to take payment!")
        else:
            print(ticket_form.errors)
            messages.error(request, f"There was an error. Please try again.")
    else:
        ticket_form = TicketForm()
        donation_form = DonationForm()
    context = {
        "donation_form": donation_form,
        "ticket_form": ticket_form,
        "publishable": settings.STRIPE_PUBLISHABLE
    }
    return render(request, "tickets_new_feature.html", context)


def tickets_view_one(request, pk):
    """ View a Single Ticket """
    # get ticket details
    ticket = get_object_or_404(Ticket, pk=pk)
    # increase number of views by 1
    ticket.views += 1
    ticket.save()
    # filter comments on specific ticket
    comments = Comment.objects.filter(ticket_id=ticket.pk)
    # filter upvotes on specific ticket by user ID
    upvotes = Upvote.objects.filter(ticket_id=ticket.pk).values("user_id")
    voters = [vote["user_id"] for vote in upvotes]
    donors = User.objects.filter(id__in=voters)
    # POST methods
    if request.method == "POST":
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
        donation_form = DonationForm()
    context = {
        "comment_form": comment_form,
        "comments": comments,
        "donation_form": donation_form,
        "donors": donors,
        "publishable": settings.STRIPE_PUBLISHABLE,
        "ticket": ticket,
        "voters": voters,
    }
    return render(request, "tickets_view_one.html", context)


@login_required
def tickets_edit(request, pk):
    """ Edit a Single Ticket """
    ticket = get_object_or_404(Ticket, pk=pk)
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
    ticket = get_object_or_404(Ticket, pk=pk)
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
    if request.method == "POST":
        donation_form = DonationForm(request.POST)
        if donation_form.is_valid():
            # amount to pay / donate
            donation_amount = 0
            donation_amount += int(request.POST.get("donation_amount"))
            try:
                # build Stripe payment
                token = request.POST["stripeToken"]
                customer = stripe.Charge.create(
                    amount=int(donation_amount * 100),
                    currency="EUR",
                    description=(
                        request.user.email +
                        " (" + request.user.get_full_name() + ")"),
                    source=token,
                )
            except stripe.error.CardError:
                # Stripe payment error
                messages.error(request, f"Your card was declined!")
            # authorization is valid - payment successful
            if customer.paid:
                Upvote.objects.create(
                    ticket_id=ticket.pk,
                    user_id=request.user.id)
                # update Ticket total donation amount
                get_total_donations = Ticket.objects.values_list(
                    "total_donations", flat=True).get(id=ticket.pk)
                new_total_donations = get_total_donations + donation_amount
                Ticket.objects.filter(
                    id=ticket.pk).update(total_donations=new_total_donations)
                # update user Profile with additional donation amount
                get_user_donations = Profile.objects.values_list(
                    "total_donated", flat=True).get(user_id=request.user.id)
                new_user_donations = get_user_donations + donation_amount
                Profile.objects.filter(
                    user_id=request.user.id).update(
                        total_donated=new_user_donations)
                # update ticket status to In Progress if €100 goal is achieved
                if new_total_donations >= int(100):
                    Ticket.objects.filter(
                        id=ticket.pk).update(ticket_status="In Progress")
                messages.success(
                    request, f"Thank You for your Donation!\
                        €{donation_amount} was charged to your card.")
                return redirect(tickets_view_one, ticket.pk)
            else:
                messages.error(request, f"Unable to take payment!")
        else:
            print(ticket_form.errors)
            messages.error(request, f"There was an error. Please try again.")
    else:
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
