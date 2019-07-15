from django.conf.urls import url
from stats.views import get_all_stats

urlpatterns = [
    url(r"^$", get_all_stats, name="get_all_stats"),
]
