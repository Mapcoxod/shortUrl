from django.urls import path

from core.views import ShortUrlCreateView, redirect_to_original, ShortUrlStatsView

urlpatterns = [
    path('', ShortUrlCreateView.as_view(), name='short-url-create'),
    path('stats/', ShortUrlStatsView.as_view(), name='short-url-stats'),
    path('<str:short_token>/', redirect_to_original, name='short-url-redirect'),
]