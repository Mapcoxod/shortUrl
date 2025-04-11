import string
import random
from django.db import models


class ShortUrl(models.Model):
    original_url = models.URLField(verbose_name="ссылка")
    short_token = models.CharField(max_length=6, unique=True, verbose_name="токен короткой ссылки")
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    clicks = models.PositiveIntegerField(default=0, verbose_name="количество переходов")

    def save(self, *args, **kwargs):
        if not self.short_token:
            self.short_token = self.generate_token()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_token():
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=6))