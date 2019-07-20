from urllib.parse import urlencode
from tickets.models import Ticket


def tickets_count(request):
    tickets_count = Ticket.objects.count()
    return {"tickets_count": tickets_count}


def get_args(request):
    args = request.GET.copy()
    if "page" in args:
        del args["page"]
    return {"get_args": "&{0}".format(args.urlencode())}


def tickets_last_five(request):
    tickets_last_five = Ticket.objects.all().order_by("-id")[:5]
    return {"tickets_last_five": tickets_last_five}
