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
