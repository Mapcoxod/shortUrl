from django.shortcuts import get_object_or_404, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy

from apps.core.forms import ShortUrlForm
from apps.core.models import ShortUrl


class ShortUrlCreateView(FormView):
    template_name = "core/create.html"
    form_class = ShortUrlForm
    success_url = reverse_lazy("short-url-create")

    def form_valid(self, form):
        original_url = form.cleaned_data["original_url"]

        short_url, created = ShortUrl.objects.get_or_create(original_url=original_url)

        context = self.get_context_data(form=form, short_url=short_url)
        return self.render_to_response(context)


def redirect_to_original(request, short_token):
    short_url = get_object_or_404(ShortUrl, short_token=short_token)
    short_url.clicks += 1
    short_url.save()
    return redirect(short_url.original_url)