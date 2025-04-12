from django import forms


class ShortUrlForm(forms.Form):
    original_url = forms.URLField(
        label="Ваша ссылка",
        widget=forms.URLInput(attrs={"placeholder": "https://example.com", "class": "form-control"})
    )