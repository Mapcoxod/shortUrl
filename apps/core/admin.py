from django.contrib import admin
from apps.core.models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'short_token', 'clicks', 'created')
    list_display_links = ('id', 'short_token')
    search_fields = ('original_url', 'short_token')
    list_filter = ('created',)
    readonly_fields = ('short_token', 'created', 'clicks')
    ordering = ('-created',)

    fieldsets = (
        (None, {
            'fields': ('original_url', 'short_token', 'clicks', 'created')
        }),
    )