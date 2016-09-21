from django.contrib import admin
from .models import Theme


class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    list_display = ('name', 'active_theme', 'description')

admin.site.register(Theme, ThemeAdmin)
