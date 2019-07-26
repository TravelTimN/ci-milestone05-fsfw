from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from accounts.models import Profile
from tickets.models import Ticket


def get_all_stats(request):
    """ Filter all necessary objects to render Statistics using Chart.js """

    """ ----- USERS ----- """
    # top 3 donors:
    users_top_three = Profile.objects.all().order_by("-total_donated")[:3]

    """ ----- MONTHLY / WEEKLY / DAILY ----- """
    date_search_start = timezone.now() - timedelta(days=30)
    date_search_end = timezone.now()

    """ ----- FEATURES ----- """
    # top 5 most voted
    features_top_five = Ticket.objects.filter(
        ticket_type="2").order_by("-upvotes")[:5]
    # total features
    features_total = Ticket.objects.filter(
        ticket_type="2").count()
    # total features 'Closed'
    features_closed = Ticket.objects.filter(
        ticket_type="2", ticket_status="3").count()
    # total features 'In Progress'
    features_in_progress = Ticket.objects.filter(
        ticket_type="2", ticket_status="2").count()
    # total features 'Open'
    features_open = Ticket.objects.filter(
        ticket_type="2", ticket_status="1").count()
    features_monthly = Ticket.objects.filter(
        date_edited__range=[date_search_start, date_search_end],
        ticket_type="2").count()
    features_weekly = round(features_monthly / 4, 2)
    features_daily = round(features_monthly / 30, 2)

    """ ----- BUGS ----- """
    # top 5 most voted
    bugs_top_five = Ticket.objects.filter(
        ticket_type="1").order_by("-upvotes")[:5]
    # total bugs
    bugs_total = Ticket.objects.filter(
        ticket_type="1").count()
    # total bugs 'Closed'
    bugs_closed = Ticket.objects.filter(
        ticket_type="1", ticket_status="3").count()
    # total bugs 'In Progress'
    bugs_in_progress = Ticket.objects.filter(
        ticket_type="1", ticket_status="2").count()
    # total bugs 'Open'
    bugs_open = Ticket.objects.filter(
        ticket_type="1", ticket_status="1").count()
    bugs_monthly = Ticket.objects.filter(
        date_edited__range=[date_search_start, date_search_end],
        ticket_type="1").count()
    bugs_weekly = round(bugs_monthly / 4, 2)
    bugs_daily = round(bugs_monthly / 30, 2)

    context = {
        "users_top_three": users_top_three,
        "features_top_five": features_top_five,
        "features_total": features_total,
        "features_closed": features_closed,
        "features_in_progress": features_in_progress,
        "features_open": features_open,
        "features_monthly": features_monthly,
        "features_weekly": features_weekly,
        "features_daily": features_daily,
        "bugs_top_five": bugs_top_five,
        "bugs_total": bugs_total,
        "bugs_closed": bugs_closed,
        "bugs_in_progress": bugs_in_progress,
        "bugs_open": bugs_open,
        "bugs_monthly": bugs_monthly,
        "bugs_weekly": bugs_weekly,
        "bugs_daily": bugs_daily,
    }
    return render(request, "statistics.html", context)
