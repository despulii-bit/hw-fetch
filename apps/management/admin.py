from django.contrib import admin

from .models import HardwareManual


@admin.register(HardwareManual)
class HardwareManualAdmin(admin.ModelAdmin):
    # What columns to show in the list view
    list_display = ("brand", "model_name", "category", "created_at")

    # Which fields are clickable to search
    search_fields = ("brand", "model_name", "model_number", "content_hash")

    # Filters on the right sidebar
    list_filter = ("category", "brand")

    # Fields that shouldn't be edited by hand
    readonly_fields = ("content_hash", "created_at", "updated_at")
