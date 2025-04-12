from django.urls import path

from core.views import ShortUrlCreateView, redirect_to_original

urlpatterns = [
    path('', ShortUrlCreateView.as_view(), name='short-url-create'),
    path('<str:short_token>/', redirect_to_original, name='short-url-redirect'),
]