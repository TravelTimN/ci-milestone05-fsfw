from tickets.models import Ticket


def tickets_count(request):
    tickets_count = Ticket.objects.count()
    return {"tickets_count": tickets_count}
