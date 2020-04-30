from django.urls import path
from stats.views import get_all_stats

urlpatterns = [
    path("", get_all_stats, name="get_all_stats"),
]
