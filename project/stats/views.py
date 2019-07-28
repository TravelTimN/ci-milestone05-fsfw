from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from accounts.models import Profile
from tickets.models import Ticket


def get_all_stats(request):
    """ Filter all necessary objects to render Statistics using Chart.js """

    # convert time/day into unix epoch timestamps
    now = int(timezone.now().timestamp())
    day = now - int(timedelta(days=1).total_seconds())
    week = now - int(timedelta(days=7).total_seconds())
    month = now - int(timedelta(days=30).total_seconds())

    """ ----- USERS ----- """
    # top 3 donors:
    users_top_three = Profile.objects.all().order_by("-total_donated")[:3]

    """ ----- BUGS ----- """
    bugs_all = Ticket.objects.filter(ticket_type=1)
    # total bugs count
    bugs_total = bugs_all.count()
    # top 5 most voted bugs
    bugs_top_five = bugs_all.order_by("-upvotes")[:5]
    bugs_status = [
        bug["ticket_status"]
        for bug in bugs_all.values("ticket_status")
    ]
    # total bugs 'Open'
    bugs_open = bugs_status.count(1)
    # total bugs 'In Progress'
    bugs_in_progress = bugs_status.count(2)
    # total bugs 'Closed'
    bugs_closed = bugs_status.count(3)
    # create list of bugs date_edited values as integer
    bugs_edited = [
        int(bug["date_edited"].timestamp())
        for bug in bugs_all.values("date_edited")]
    # total number of bugs edited in last day
    bugs_daily = len(list(
        bug for bug in bugs_edited if bug in range(day, now)))
    # total number of bugs edited in last week
    bugs_weekly = len(list(
        bug for bug in bugs_edited if bug in range(week, now)))
    # total number of bugs edited in last month
    bugs_monthly = len(list(
        bug for bug in bugs_edited if bug in range(month, now)))

    """ ----- FEATURES ----- """
    features_all = Ticket.objects.filter(ticket_type=2)
    # total features count
    features_total = features_all.count()
    # top 5 most voted features
    features_top_five = features_all.order_by("-upvotes")[:5]
    features_status = [
        feature["ticket_status"]
        for feature in features_all.values("ticket_status")
    ]
    # total features 'Open'
    features_open = features_status.count(1)
    # total features 'In Progress'
    features_in_progress = features_status.count(2)
    # total features 'Closed'
    features_closed = features_status.count(3)
    # create list of features date_edited values as integer
    features_edited = [
        int(feature["date_edited"].timestamp())
        for feature in features_all.values("date_edited")]
    # total number of features edited in last day
    features_daily = len(list(
        feature for feature in features_edited
        if feature in range(day, now)))
    # total number of features edited in last week
    features_weekly = len(list(
        feature for feature in features_edited
        if feature in range(week, now)))
    # total number of features edited in last month
    features_monthly = len(list(
        feature for feature in features_edited
        if feature in range(month, now)))

    context = {
        "users_top_three": users_top_three,
        "bugs_total": bugs_total,
        "bugs_top_five": bugs_top_five,
        "bugs_open": bugs_open,
        "bugs_in_progress": bugs_in_progress,
        "bugs_closed": bugs_closed,
        "bugs_daily": bugs_daily,
        "bugs_weekly": bugs_weekly,
        "bugs_monthly": bugs_monthly,
        "features_total": features_total,
        "features_top_five": features_top_five,
        "features_open": features_open,
        "features_in_progress": features_in_progress,
        "features_closed": features_closed,
        "features_daily": features_daily,
        "features_weekly": features_weekly,
        "features_monthly": features_monthly,
    }
    return render(request, "statistics.html", context)
