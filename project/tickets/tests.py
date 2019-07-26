from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse, get_object_or_404
from tickets.forms import TicketForm, DonationForm, CommentForm
from tickets.models import Ticket


# ----- FORMS ----- #
class TestTicketForm(TestCase):
    def test_users_can_create_a_new_ticket(self):
        form = TicketForm(
            {"title": "My New Test Ticket",
                "description": "My test description of a fake Bug!"})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = TicketForm({"description": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["description"], [u"This field is required."])


class TestDonationForm(TestCase):
    def test_donation_value_is_valid(self):
        form = DonationForm({"donation_amount": 10})
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    def test_comment_is_not_long_enough(self):
        form = CommentForm({"comment": "test"})
        self.assertFalse(form.is_valid())

    def test_comment_is_long_enough(self):
        form = CommentForm({"comment": "test comment"})
        self.assertTrue(form.is_valid())


# ----- VIEWS ----- #
class TestTicketsViews(TestCase):
    def setUp(self):
        Ticket.objects.create(
            title="Test Bug",
            description="Test description on new Bug Ticket",
            ticket_status=1,
            ticket_type=1).save()
        Ticket.objects.create(
            title="Test Feature",
            description="Test description on new Feature Ticket",
            ticket_status=1,
            ticket_type=2).save()
        self.client.post(
            "/accounts/register/",
            {"email": "Test@Email.com",
                "username": "TestUser",
                "first_name": "TestFirst",
                "last_name": "TestLast",
                "password1": "Passw0rd",
                "password2": "Passw0rd"})

    def test_tickets_view_all(self):
        page = self.client.get("/tickets/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "tickets_view_all.html")

    def test_tickets_view_one(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        response = self.client.get(
            "/tickets/{0}".format(ticket.pk), follow=True)
        self.assertIn(b"Sound familiar? Let us know!", response.content)

    def test_tickets_new_bug(self):
        self.client.post(
            "/tickets/new/bug",
            {"title": "Test Another Bug",
                "description": "Test description on another Bug Ticket",
                "ticket_status": "Open",
                "ticket_type": "Bug"})
        ticket = Ticket.objects.filter(title="Test Another Bug")[0]
        self.assertEqual("Test Another Bug", ticket.title)

    def test_tickets_upvote_bug(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        upvotes = ticket.upvotes
        self.assertEqual(upvotes, 0)
        self.client.get(
            "/tickets/upvote/add/{0}".format(ticket.pk), follow=True)
        upvote_add = Ticket.objects.filter(title="Test Bug")[0].upvotes
        self.assertEqual(upvote_add, 1)

    def test_tickets_upvote_remove(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        upvotes = ticket.upvotes
        self.assertEqual(upvotes, 0)
        self.client.get(
            "/tickets/upvote/add/{0}".format(ticket.pk), follow=True)
        upvote_add = Ticket.objects.filter(title="Test Bug")[0].upvotes
        self.client.get(
            "/tickets/upvote/remove/{0}".format(ticket.pk), follow=True)
        upvote_remove = Ticket.objects.filter(title="Test Bug")[0].upvotes
        self.assertEqual(upvote_remove, 0)

    def test_tickets_upvote_feature_with_payment(self):
        ticket = Ticket.objects.filter(title="Test Feature")[0]
        response = self.client.get(
            "/tickets/{0}#modal-feature-payment".format(ticket.pk),
            follow=True)
        self.assertIn(
            b"Important: Upvote Payments are Non-Refundable!",
            response.content)

    def test_tickets_edit(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        response = self.client.get(
            "/tickets/edit/{0}".format(ticket.pk), follow=True)
        self.assertIn(
            b'<label class="" for="id_title">Title of Ticket</label>',
            response.content)

    def test_tickets_edit_saved(self):
        ticket = Ticket.objects.filter(
            description="Test description on new Bug Ticket")[0]
        self.assertEqual(ticket.title, "Test Bug")
        self.client.post("/tickets/edit/{0}".format(ticket.pk), data={
            "title": "Test Bug Updated",
            "description": "Test description on new Bug Ticket"}, follow=True)
        new_ticket_title = Ticket.objects.filter(
            description="Test description on new Bug Ticket")[0].title
        self.assertEqual(new_ticket_title, "Test Bug Updated")

    def test_tickets_delete(self):
        ticket = Ticket.objects.filter(title="Test Bug")[0]
        response = self.client.get(
            "/tickets/{0}".format(ticket.pk), follow=True)
        results = Ticket.objects.filter(
            description="Test description on new Bug Ticket").count()
        self.assertEqual(results, 1)
        self.client.get("/tickets/delete/{0}".format(ticket.pk), follow=True)
        tickets_delete = Ticket.objects.filter(title="Test Bug").count()
        self.assertEqual(tickets_delete, 0)
