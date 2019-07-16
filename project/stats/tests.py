from django.test import TestCase


# ----- VIEWS ----- #
class TestGetAllStats(TestCase):
    def test_get_all_stats(self):
        page = self.client.get("/statistics/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "statistics.html")
