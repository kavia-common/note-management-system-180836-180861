from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Admin configuration for Note."""
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title", "content")
    ordering = ("-updated_at",)
